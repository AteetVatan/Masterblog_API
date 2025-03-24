"""The main file for Master Blog API."""
from flask import Flask
from flask_cors import CORS

from controllers import AppController

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app_controller = AppController(app)
    app_controller.app.run(host="0.0.0.0", port=5002, debug=True, use_reloader=False)
