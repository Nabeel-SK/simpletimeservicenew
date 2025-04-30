from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Define Indian timezone
india_timezone = pytz.timezone('Asia/Kolkata')

@app.route("/", methods=["GET"])
def get_time():
    visitor_ip = request.remote_addr
    current_time = datetime.now(india_timezone).isoformat()
    return jsonify({
        "timestamp": current_time,
        "ip": visitor_ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

