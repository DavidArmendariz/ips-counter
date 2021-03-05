from flask import Flask, request, jsonify

from .clear_data import clear_data
from .store_ip import store_ip
from .get_top_k_ips import get_top_k_ips

app = Flask(__name__)


@app.route("/")
def request_handled():
    ip = request.remote_addr
    store_ip(ip)
    return f"Welcome!"


@app.route("/top")
def top():
    largest = get_top_k_ips()
    return jsonify(largest)


@app.route("/clear")
def clear():
    clear_data()
    return "Data cleared successfully"