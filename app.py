from __init__ import create_app
from controllers.router import httpController
from flask_cors import CORS
import threading
import time


app = create_app()
CORS(httpController, resources={r"/api/stock/*": {"origins": "*"}})
app.register_blueprint(httpController)


def mosquitto_loop():
  while True:
    app.config['client'].loop()
    time.sleep(1) 

if __name__ == "__main__":
  mosquitto_thread = threading.Thread(target=mosquitto_loop)
  mosquitto_thread.start()
  app.run(host="localhost", port=5000, debug=True)