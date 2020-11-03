import eventlet
import json
from flask import Flask, render_template
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
            SENSOR CHAR(255) PRIMARY KEY    NOT NULL,
            VALUE           FLOAT           NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('pressure',))
pressureTable = bool(cur.rowcount)

if not pressureTable:
    cur.execute('''CREATE TABLE pressure
        (
            SENSOR CHAR(255) PRIMARY KEY    NOT NULL,
            VALUE           FLOAT           NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('temperature',))
temperatureTable = bool(cur.rowcount)

if not temperatureTable:
    cur.execute('''CREATE TABLE temperature
        (
            SENSOR CHAR(255) PRIMARY KEY    NOT NULL,
            VALUE           FLOAT           NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('airquality',))
airqualityTable = bool(cur.rowcount)

if not airqualityTable:
    cur.execute('''CREATE TABLE airquality
        (
            SENSOR CHAR(255) PRIMARY KEY    NOT NULL,
            VALUE           INT             NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')

cur.execute("select * from information_schema.tables where table_name=%s", ('gps',))
gpsTable = bool(cur.rowcount)

if not gpsTable:
    cur.execute('''CREATE TABLE gps
        (
            SENSOR CHAR(255) PRIMARY KEY    NOT NULL,
            VALUE           TEXT []         NOT NULL,
            TIMESTAMP       TIMESTAMP       NOT NULL
        ); ''')
      

print("Hallo")
con.commit()
con.close()

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe(ATT_SUB_TOPIC)

@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    print("Payload: " + payload)
    if message.topic == topics.get("humidity"):
        cur.execute("INSERT INTO humidity (SENSOR,VALUE,TIMESTAMP) VALUES (%s, %s, %s)",  (topics.get('humidity'), payload["value"], payload["at"]))
        con.commit()

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