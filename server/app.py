import eventlet
import json
from flask import Flask, render_template, jsonify
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin
from configuration import Config
import psycopg2

eventlet.monkey_patch()

DEBUG = True

app = Flask(__name__)
app.config.from_object(Config())

ATT_DEVICE_ID = app.config['ATT_DEVICE_ID']
ATT_SUB_TOPIC ="device/" + ATT_DEVICE_ID + "/asset/#"

topics = {
    "humidity": "device/" + ATT_DEVICE_ID + "/asset/humidity/feed",
    "pressure": "device/" + ATT_DEVICE_ID + "/asset/pressure/feed",
    "temperature": "device/" + ATT_DEVICE_ID + "/asset/temperature/feed",
    "airquality": "device/" + ATT_DEVICE_ID + "/asset/air_quality/feed",
    "gps": "device/" + ATT_DEVICE_ID + "/asset/gps/feed",
}

cors = CORS(app, resources={r"/*": {"origins": "*"}})
mqtt = Mqtt(app)
socketio = SocketIO(app, cors_allowed_origins='*')
bootstrap = Bootstrap(app)

con = psycopg2.connect(database="ATT", user="11800991", password="admin123", host="127.0.0.1", port="5432")
print("Connected to db")

cur = con.cursor()

cur.execute("select * from information_schema.tables where table_name=%s", ('humidity',))
humidityTable = bool(cur.rowcount)

## Refactor to new file

if not humidityTable:
    cur.execute('''CREATE TABLE humidity
        (
            VALUE           FLOAT           NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('pressure',))
pressureTable = bool(cur.rowcount)

if not pressureTable:
    cur.execute('''CREATE TABLE pressure
        (
            VALUE           FLOAT           NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('temperature',))
temperatureTable = bool(cur.rowcount)

if not temperatureTable:
    cur.execute('''CREATE TABLE temperature
        (
            VALUE           FLOAT           NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('airquality',))
airqualityTable = bool(cur.rowcount)

if not airqualityTable:
    cur.execute('''CREATE TABLE airquality
        (
            VALUE           FLOAT             NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('gps',))
gpsTable = bool(cur.rowcount)

if not gpsTable:
    cur.execute('''CREATE TABLE gps
        (
            TIMESTAMP       TIMESTAMP       NOT NULL,
            LAT             FLOAT           NOT NULL,
            LONG            FLOAT           NOT NULL,
            ALT             FLOAT           NOT NULL
        ); ''')
      
con.commit()

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe(ATT_SUB_TOPIC)

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@app.route('/api/humidity', methods=['GET'])
def humidity():
    cur.execute("SELECT * FROM humidity")
    records = cur.fetchall()
    return jsonify(records)

@app.route('/api/pressure', methods=['GET'])
def pressure():
    cur.execute("SELECT * FROM pressure")
    records = cur.fetchall()
    return jsonify(records)

@app.route('/api/temperature', methods=['GET'])
def temperature():
    cur.execute("SELECT * FROM temperature")
    records = cur.fetchall()
    return jsonify(records)

@app.route('/api/airquality', methods=['GET'])
def airquality():
    cur.execute("SELECT * FROM airquality")
    records = cur.fetchall()
    return jsonify(records)

@app.route('/api/gps', methods=['GET'])
def gps():
    cur.execute("SELECT * FROM gps")
    records = cur.fetchall()
    return jsonify(records)

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
            print(message.payload.decode())
        
    elif message.topic == topics.get("pressure"):
        socketio.emit('pressure', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO pressure (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print(message.payload.decode())
        
    elif message.topic == topics.get("temperature"):
        socketio.emit('temperature', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO temperature (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print(message.payload.decode())

    elif message.topic == topics.get("airquality"):
        socketio.emit('airquality', data=payload)
        payload_str = payload.split('"')
        payload_val = payload_str[6][1:-1]
        payload_time = payload_str[3]
        cur.execute("INSERT INTO airquality (VALUE,TIMESTAMP) VALUES (%s, %s)",  (payload_val, payload_time))
        con.commit()
        if DEBUG:
            print(message.payload.decode())
            
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
            print(message.payload.decode())

if __name__ == '__main__':
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=True)