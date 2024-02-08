import os
from flask import Flask, current_app as app
import paho.mqtt.client as mqtt
from controllers.mqtt_controller import on_connect, on_message, on_publish, on_subscribe
from flask_cors import CORS
from controllers.sqlite_controller import create_table
import time

#Initializes the application for use

def create_app():
  app = Flask(__name__, static_folder='./templates/', static_url_path='/')
  CORS(app)
  
  app.config.from_mapping(
      SECRET_KEY='dev',
      DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  )
  
  create_table()

  broker_address = "localhost"
  PORT = 1883
  topic = 'pc2plc'
  client = mqtt.Client(client_id="pc", userdata=None, protocol=mqtt.MQTTv5)
  client.on_connect = on_connect
  client.on_message = on_message
  client.on_publish = on_publish
  client.on_subscribe = on_subscribe
  client.connect(broker_address, PORT, 60)
  client.subscribe(topic)

  app.config['client'] = client
  app.config['topic'] = topic

  return app
