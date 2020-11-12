import eventlet
import json
from flask import Flask, render_template, jsonify, send_from_directory
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
from configuration import Config
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import psycopg2
from DbTableConfig import create_tables, create_database
import os
import urllib.parse as urlparse
from psycopg2.extras import RealDictCursor
import pandas
import zipfile

eventlet.monkey_patch()

DEBUG = False

app = Flask(__name__, static_folder = "./dist/static", template_folder="./dist")
app.config.from_object(Config())

ATT_DEVICE_ID = app.config['ATT_DEVICE_ID']
ATT_SUB_TOPIC ="device/" + ATT_DEVICE_ID + "/asset/#"

topics = {
    "humidity": "device/" + ATT_DEVICE_ID + "/asset/humidity/feed",
    "pressure": "device/" + ATT_DEVICE_ID + "/asset/pressure/feed",
    "temperature": "device/" + ATT_DEVICE_ID + "/asset/temperature/feed",
    "airquality": "device/" + ATT_DEVICE_ID + "/asset/air_quality/feed",
    "gps": "device/" + ATT_DEVICE_ID + "/asset/gps/feed",
    "loudness": "device/" + ATT_DEVICE_ID + "/asset/loudness/feed",
    "light": "device/" + ATT_DEVICE_ID + "/asset/light/feed",
    "motion": "device/" + ATT_DEVICE_ID + "/asset/motion/feed",
    "pm1": "device/" + ATT_DEVICE_ID + "/asset/pm1/feed",
    "pm10": "device/" + ATT_DEVICE_ID + "/asset/pm10/feed",
    "pm25": "device/" + ATT_DEVICE_ID + "/asset/pm25/feed",
}

if not app.config['ENV'] == "production":
    cors = CORS(app, resources={r"*": {"origins": "*"}})
else:
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


mqtt = Mqtt(app)
bootstrap = Bootstrap(app)

if not app.config['ENV'] == "production":
    socketio = SocketIO(app, cors_allowed_origins='*')
    create_database(DEBUG=DEBUG)
    con = psycopg2.connect(database="att", user="11800991", password="admin123", host="127.0.0.1", port="5432")
else:
    socketio = SocketIO(app, cors_allowed_origins='0.0.0.0')
    dbUrl = urlparse.urlparse(os.environ['DATABASE_URL'])
    dbName = dbUrl.path[1:]
    dbUser = dbUrl.username
    dbPassword = dbUrl.password
    dbHost = dbUrl.hostname
    dbPort = dbUrl.port
    con = psycopg2.connect(database=dbName, user=dbUser, password=dbPassword, host=dbHost, port=dbPort)

if DEBUG:
    print("[INFO] - Connected to DB att.")
    
cur = con.cursor(cursor_factory=RealDictCursor)
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
create_tables(cur=cur, DEBUG=DEBUG)

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe(ATT_SUB_TOPIC)

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

def createCSVFile(sensor):
    fn = "export/" + sensor + '.csv'
    cur.execute("SELECT * FROM " + sensor)
    records = cur.fetchall()
    pandas.DataFrame(records).to_csv(fn, index=False)


@app.route('/api/download', methods=['GET'])
def export_csv():
    createCSVFile('temperature')
    createCSVFile('humidity')
    createCSVFile('pressure')
    createCSVFile('airquality')
    createCSVFile('gps')
    createCSVFile('light')
    createCSVFile('gps')
    createCSVFile('loudness')
    createCSVFile('motion')

    zipf = zipfile.ZipFile('archives/export.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('export/', zipf)
    zipf.close()
    return send_from_directory('archives', 'export.zip', attachment_filename='export.zip', as_attachment=True)

@app.route('/api/humidity', methods=['GET'])
def humidity():
    cur.execute("SELECT * FROM humidity")
    return jsonify(cur.fetchall())

@app.route('/api/pressure', methods=['GET'])
def pressure():
    cur.execute("SELECT * FROM pressure")
    return jsonify(cur.fetchall())

@app.route('/api/temperature', methods=['GET'])
def temperature():
    cur.execute("SELECT * FROM temperature")
    return jsonify(cur.fetchall())

@app.route('/api/airquality', methods=['GET'])
def airquality():
    cur.execute("SELECT * FROM airquality")
    return jsonify(cur.fetchall())

@app.route('/api/gps', methods=['GET'])
def gps():
    cur.execute("SELECT * FROM gps")
    return jsonify(cur.fetchall())

@app.route('/api/light', methods=['GET'])
def light():
    cur.execute("SELECT * FROM light")
    return jsonify(cur.fetchall())

@app.route('/api/loudness', methods=['GET'])
def loudness():
    cur.execute("SELECT * FROM loudness")
    return jsonify(cur.fetchall())

@app.route('/api/motion', methods=['GET'])
def motion():
    cur.execute("SELECT * FROM motion")
    return jsonify(cur.fetchall())


@app.route('/api/humidity/<amount>', methods=['GET'])
def humidityAm(amount):
    cur.execute("SELECT * FROM humidity ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())

@app.route('/api/pressure/<amount>', methods=['GET'])
def pressureAm(amount):
    cur.execute("SELECT * FROM pressure ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())

@app.route('/api/temperature/<amount>', methods=['GET'])
def temperatureAm(amount):
    cur.execute("SELECT * FROM temperature ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())

@app.route('/api/airquality/<amount>', methods=['GET'])
def airqualityAm(amount):
    cur.execute("SELECT * FROM airquality ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())

@app.route('/api/gps/<amount>', methods=['GET'])
def gpsAm(amount):
    cur.execute("SELECT * FROM gps ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())

@app.route('/api/light/<amount>', methods=['GET'])
def lightAm(amount):
    cur.execute("SELECT * FROM light ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())

@app.route('/api/loudness/<amount>', methods=['GET'])
def loudnessAm(amount):
    cur.execute("SELECT * FROM loudness ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())

@app.route('/api/motion/<amount>', methods=['GET'])
def motionAm(amount):
    cur.execute("SELECT * FROM motion ORDER BY TIMESTAMP DESC LIMIT " + amount + ";")
    return jsonify(cur.fetchall())


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    if message.topic == topics.get("humidity"):
        socketio.emit('humidity', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO humidity (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print("Humidity:" + message.payload.decode())
        
    elif message.topic == topics.get("pressure"):
        socketio.emit('pressure', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO pressure (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print("Pressure:" + message.payload.decode())
        
    elif message.topic == topics.get("temperature"):
        socketio.emit('temperature', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO temperature (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print("Temperature:" + message.payload.decode())

    elif message.topic == topics.get("airquality"):
        socketio.emit('airquality', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO airquality (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print("Airquality:" + message.payload.decode())

    elif message.topic == topics.get("gps"):
        socketio.emit('gps', data=payload)
        payload_str = payload.split('"')
        payload_time = payload_str[3]
        payload_lat = payload_str[8][1:-1]
        payload_long = payload_str[10][1:-2]
        payload_alt = payload_str[12][1:-2]
        cur.execute("INSERT INTO gps (TIMESTAMP,LAT,LONG,ALT) VALUES (%s, %s, %s, %s)",  (payload_time, payload_lat, payload_long, payload_alt))
        con.commit()
        if DEBUG:
            print("GPS:" + message.payload.decode())
    
    elif message.topic == topics.get("light"):
        socketio.emit('light', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO light (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print("Light:" + message.payload.decode())

    elif message.topic == topics.get("loudness"):
        socketio.emit('loudness', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO loudness (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print("Loudness:" + message.payload.decode())

    elif message.topic == topics.get("motion"):
        socketio.emit('motion', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO motion (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print("Motion:" + message.payload.decode())

    
    else:
        print(message.payload.decode())
        print("Hello")


if __name__ == '__main__':
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app, host='0.0.0.0', port=app.config['PORT'], use_reloader=False, debug=DEBUG)