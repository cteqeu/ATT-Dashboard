# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

# Smartphone has following assets:
#   battery         (sensor)    => number
#   message         (actuator)  => string
#   sending_data    (sensor)    => boolean
#   orientation     (sensor)    => object (alpha, beta, gamma)
#   movement        (sensor)    => string
#   color           (actuator)  => string
#   location        (location)  => object (lat number, long number)
#   shake           (location)  => boolean


class Config(object):
    ENV = "dev"
    PORT = 3000
    ATT_DEVICE_ID = "fO7K0gYRpEMJmY1PDy5cSpzh"
    SECRET = 'cQfTjWnZr4u7x!A%D*G-KaPdSgUkXp2s'
    TEMPLATES_AUTO_RELOAD = True
    MQTT_BROKER_URL = "api.allthingstalk.io"
    MQTT_BROKER_PORT = 1883
    MQTT_USERNAME = "maker:4H0f8zZfr9kSG0lqFujuiTclythuwmZx1ZNiMo8"
    MQTT_PASSWORD = 'xxxxxx'
    MQTT_KEEPALIVE = 5
    MQTT_TLS_ENABLED = False
    MQTT_CLEAN_SESSION = True