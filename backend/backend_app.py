"""The main file for Master Blog API."""
import os
import sys

from flask import Flask
from flask_cors import CORS

from backend.controllers import AppController
from backend.helpers import PortHelper

app = Flask(__name__)
CORS(app)
#Python will treat backend/ as a root
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == '__main__':
    app_controller = AppController(app)
    PORT = 5002
    port_helper = PortHelper()
    port_helper.check_port(PORT)
    app_controller.app.run(host="0.0.0.0", port=PORT, debug=True, use_reloader=False)
