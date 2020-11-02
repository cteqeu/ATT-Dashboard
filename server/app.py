import eventlet
import json
from flask import Flask, render_template, jsonify, request, session, redirect
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
import json

from services.auth import Auth
from models.defaultMethodResult import DefaultMethodResult
from models.loginTokenResult import LoginTokenResult
from services.jsonClassEncoder import JsonClassEncoder
import flask_login
from flask_login import user_loaded_from_header
from services.customSessionInterface import CustomSessionInterface


eventlet.monkey_patch()

# Smartphone has following assets:
#   battery         (sensor)    => number
#   message         (actuator)  => string
#   sending_data    (sensor)    => boolean
#   orientation     (sensor)    => object (alpha, beta, gamma)
#   movement        (sensor)    => string
#   color           (actuator)  => string
#   location        (location)  => object (lat number, long number)
#   shake           (location)  => boolean

DEBUG = False

SECRET = 'cQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s'
BROKER_URL = "api.allthingstalk.io"
BROKER_PORT = 1883
ATT_DEVICE_TOKEN = "maker:4H0f8zZfr9kSG0lqFujuiTclythuwmZx1ZNiMo8"
ATT_DEVICE_ID = "fO7K0gYRpEMJmY1PDy5cSpzh"
ATT_SUB_TOPIC ="device/" + ATT_DEVICE_ID + "/asset/#"
ATT_TEMP_SUB_TOPIC = "device/" + ATT_DEVICE_ID + "/asset/temperature/feed"

# Configurations
ALOWED_CORS_DOMAIN = 'http://localhost:8080'
app = Flask(__name__)
app.config['SECRET'] = SECRET
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = BROKER_URL
app.config['MQTT_BROKER_PORT'] = BROKER_PORT
app.config['MQTT_USERNAME'] = ATT_DEVICE_TOKEN
app.config['MQTT_PASSWORD'] = 'xxxxxx'
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLEAN_SESSION'] = True

topics = {
    "humidity": "device/fO7K0gYRpEMJmY1PDy5cSpzh/asset/humidity/feed",
    "pressure": "device/fO7K0gYRpEMJmY1PDy5cSpzh/asset/pressure/feed",
    "temperature": "device/fO7K0gYRpEMJmY1PDy5cSpzh/asset/temperature/feed",
    "airquality": "device/fO7K0gYRpEMJmY1PDy5cSpzh/asset/air_quality/feed",
    "gps": "device/fO7K0gYRpEMJmY1PDy5cSpzh/asset/gps/feed",
}

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

CORS(app, resources=r'/*')
mqtt = Mqtt(app)
socketio = SocketIO(app, cors_allowed_origins='*')
bootstrap = Bootstrap(app)
authModule = Auth()
jsonClassEncoder = JsonClassEncoder()
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.session_interface = CustomSessionInterface()

@login_manager.user_loader
def load_user(user_id):
    return authModule.load_user(user_id)

# Only requests that have an Authorization request reader set with a valid login token
# can access the protected routes, like this '/home' one for example
@app.route('/', methods=(['GET']))
@flask_login.login_required
def home():
    return 'Home protected by @flask_login.login_required'

@app.route('/register', methods=(['POST']))
def register():
    requestPayload = request.get_json()  
    username = requestPayload['email']
    password = requestPayload['password']
    mobilePhone= requestPayload['mobilePhone']

    registerResult = authModule.register(username, password, mobilePhone)
    if registerResult.success == True:
        return jsonClassEncoder.encode(registerResult), 200
    else:
        return jsonClassEncoder.encode(registerResult), 500

# this route will login the user and return a Json Web Token, this token 
# will be stored into the client aplication and need to be passed over for each new 
# request, via Authorizaton header.
@app.route('/token', methods=(['POST']))
def token():
    authToken = request.headers.get('Authorization')
    activeSession = authModule.GetActiveSession(authToken)
    if activeSession is not None:
        loginResult = LoginTokenResult(True, 'Login successful', activeSession.jwToken)
        return jsonClassEncoder.encode(loginResult), 200
    else:
        requestPayload = request.get_json()  
        username = requestPayload['email']
        password = requestPayload['password']
        loginResult = authModule.getLoginToken(username, password, app.config['SECRET_KEY'])
        if loginResult.success == True:
            return jsonClassEncoder.encode(loginResult), 200
        else:
            return jsonClassEncoder.encode(loginResult), 401

# This will invalidate the user current user session on the server
@app.route('/logout', methods=(['POST']))
def sessionLogout():
    authToken = request.headers.get('Authorization')
    logoutResult = authModule.SessionLogout(authToken, request.url)
    if logoutResult.success == True:        
        return jsonClassEncoder.encode(logoutResult), 200
    else:
        return jsonClassEncoder.encode(logoutResult), 401

# This enable CORS, it means that this server will authorize AJAX calls from
# other domains than the current domain where the API is running
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = ALOWED_CORS_DOMAIN
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers

    return response

app.after_request(add_cors_headers)

# Checks if the user is auhenticated for protected routes decorated with @flask_login.login_required
@login_manager.request_loader
def load_user_from_request(request):
    # Get the token from the Authorization request header 
    authToken = request.headers.get('Authorization')
    if authToken:
        try:
            # Checks if is there a active session for this token and return his user
            user = authModule.GetUserByToken(authToken)
            return user
        except TypeError:
            pass        

    # If it can't find an active session returns None, 
    # this will cause the request decorated with @flask_login.login_required been denied
    return None


@socketio.on('publish')
def handle_publish(json_str):
    pass

@socketio.on('subscribe')
def handle_subscribe(json_str):
   pass

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe(ATT_SUB_TOPIC)
    print('connected')

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()

    if message.topic == topics.get("humidity"):
        socketio.emit('humidity', data=payload)
        if DEBUG:
            print(message.payload.decode())
        
    elif message.topic == topics.get("pressure"):
        socketio.emit('pressure', data=payload)
        if DEBUG:
            print(message.payload.decode())
        
    elif message.topic == topics.get("temperature"):
        socketio.emit('temperature', data=payload)
        if DEBUG:
            print(message.payload.decode())

    elif message.topic == topics.get("airquality"):
        socketio.emit('airquality', data=payload)
        if DEBUG:
            print(message.payload.decode())
            
    elif message.topic == topics.get("gps"):
        socketio.emit('gps', data=payload)
        if DEBUG:
            print(message.payload.decode())

# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#     print(level, buf)


if __name__ == '__main__':
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)