import paho.mqtt.client as mqtt
from flask import current_app as app

#Controls warehouse inbound and outbound with PLC through MQTT router

# Funktio, joka ajetaan, kun yhteys muodostetaan
def on_connect(mqttclient, obj, flags, rc, properties=None):
  print("Connected with result code: " + str(rc))

# Funktio, joka ajetaan aina, kun viesti saapuu
def on_message(mqttclient, obj, msg):
  print(msg.topic + " | " + str(msg.payload))
    
# Funktio, joka ajetaan, kun julkaistaan
def on_publish(mqttclient, obj, mid, properties=None):
  print("mid: " + str(mid))

# Tilauksen yhteydessä ajettava funktio
def on_subscribe(mqttclient, obj, mid, granted_qos, properties=None):
  print("Tilaus: " + str(mid) + " " + str(granted_qos))

