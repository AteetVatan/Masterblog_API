"""The Main Frontend Module"""
from flask import Flask, render_template
import frontend.config as config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """The index API end point."""
    return render_template("index.html",
                           api_default_url=config.DEFAULT_API_BASE_URL)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=False)
