from flask import Flask, Blueprint, render_template, request, jsonify, current_app as app
from controllers.sqlite_controller import add_to_table, get_all, remove_item, get_location
import json

httpController = Blueprint('httpController', __name__)


@httpController.route('/', methods=['GET'])
def index():
  return app.send_static_file('index.html')

@httpController.route('/api/stock', methods=['GET'])
def get_stock():
  try:
    stock = get_all()
    return stock
  except:
    return "Database error"

@httpController.route('/api/stock', methods=['POST'])
def add_to_stock():
  try:
    data = request.json
    client = app.config['client']
    topic = app.config['topic']
    inbound_dock = 0
    message = json.dumps({
      "A": inbound_dock,
      "B": data['location']
    })
    client.publish(topic, message)
    client.loop()    
    result = add_to_table(data['name'], data['description'], data['location'])
    return result
  except Exception as err:
    return jsonify({"status": "error", "message": str(err)})


@httpController.route('/api/stock/<id>', methods=['DELETE'])
def order_item(id):
  try:
    location = get_location(id)
    outbound_dock = 10
    message = json.dumps({
      "A": location,
      "B": outbound_dock
    })
    client = app.config['client']
    topic = app.config['topic']
    client.publish(topic, message)
    client.loop()
    result = remove_item(id)
    return jsonify(result)
  except Exception as e:
    return jsonify({"status": "error", "message": str(e)})

@httpController.route('/mqttmsg', methods=['POST'])
def post_msg():
  try:
    client = app.config['client']
    topic = app.config['topic']
    data = request.json
    message = str(data)
    print(message)
    print('publishing to topic:', topic, 'client:', client)
    client.publish(topic, message)
    client.loop()
    return jsonify({"status": "success"})
  except Exception as err:
    return jsonify({"status": "error", "message": str(err)})
