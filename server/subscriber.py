import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt

BROKER_URL = "api.allthingstalk.io"
BROKER_PORT = 1883
ATT_DEVICE_TOKEN = "maker:4H0f8zZfr9kSG0lqFujuiTclythuwmZx1ZNiMo8"
ATT_DEVICE_ID = "fO7K0gYRpEMJmY1PDy5cSpzh"
ATT_SUB_TOPIC ="device/" + ATT_DEVICE_ID + "/asset/#"
ATT_TEMP_SUB_TOPIC = "device/" + ATT_DEVICE_ID + "/asset/temperature/feed"

# Smartphone has following assets:
#   battery         (sensor)    => number
#   message         (actuator)  => string
#   sending_data    (sensor)    => boolean
#   orientation     (sensor)    => object (alpha, beta, gamma)
#   movement        (sensor)    => string
#   color           (actuator)  => string
#   location        (location)  => object (lat number, long number)
#   shake           (location)  => boolean

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("[INFO] - Connected to: " + BROKER_URL + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe(ATT_TEMP_SUB_TOPIC)
    print("[INFO] - Subscribed to: " + ATT_TEMP_SUB_TOPIC);

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload) + "\n")

client = mqtt.Client()  
client.username_pw_set(ATT_DEVICE_TOKEN, password='xxxxx')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_URL, BROKER_PORT, 60)
client.loop_forever()