from flask import Flask, jsonify, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# POSTS = [
#     {"id": 1, "title": "First post", "content": "This is the first post."},
#     {"id": 2, "title": "Second post", "content": "This is the second post."},
# ]

@app.route('/')
def index():
    end_point = "get_posts"
    return redirect(url_for(end_point))

@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True,  use_reloader=False)
