from gevent import monkey

monkey.patch_all()

from flask import Flask
from gevent import pywsgi

app = Flask(__name__)


@app.route("/")
def index():
    return "success"


if __name__ == "__main__":
    # app.run()
    server = pywsgi.WSGIServer(
        ("0.0.0.0", 8888), app)
    server.serve_forever()
