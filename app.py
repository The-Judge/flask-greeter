# Test Project for IA Nuxt replacement
# See https://earthly.dev/blog/setup-reverse-proxy-kubernetes-nginx/
# and #302354 for Details
import os
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return f'Hello from {os.getenv("HELLO_NAME", "Flask")}!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
