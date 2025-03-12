# Test Project for IA Nuxt replacement
# See https://earthly.dev/blog/setup-reverse-proxy-kubernetes-nginx/
# and #302354 for Details
import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    return f'Hello from {os.getenv("HELLO_NAME", "Flask")}, serving "{request.url}"!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
