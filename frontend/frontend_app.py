"""The Main Frontend Module"""
from flask import Flask, render_template
import frontend.config as config
from frontend.helpers import PortHelper

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """The index API end point."""
    return render_template("index.html",
                           api_default_url=config.DEFAULT_API_BASE_URL)


if __name__ == '__main__':
    PORT = 5001
    port_helper = PortHelper()
    port_helper.check_port(PORT)
    app.run(host="0.0.0.0", port=PORT, debug=True, use_reloader=False)
