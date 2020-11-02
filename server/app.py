import eventlet
import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin

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

cors = CORS(app, resources={r"/*": {"origins": "*"}})
mqtt = Mqtt(app)
socketio = SocketIO(app, cors_allowed_origins='*')
bootstrap = Bootstrap(app)

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

if __name__ == '__main__':
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)