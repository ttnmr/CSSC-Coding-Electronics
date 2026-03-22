from flask import Flask, render_template, jsonify
from picamera2 import Picamera2
import time
import os
import random

app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

# Initialize Camera
picam2 = Picamera2()
picam2.start()

# --- THE DATA ROUTE (This fixes the 404 error) ---
@app.route("/data")
def data():
    # Mock data for testing - replace with your sensor variables later
    values = {
        "temp": round(random.uniform(21.0, 23.0), 1),
        "humidity": round(random.uniform(40.0, 50.0), 1),
        "pressure": round(random.uniform(1010.0, 1015.0), 1)
    }
    return jsonify(values)

@app.route("/")
def index():
    return render_template("index.html", temp=22.0, humidity=45, pressure=1013)

@app.route("/capture")
def capture():
    filename = "static/photo.jpg"
    picam2.capture_file(filename)
    return jsonify({"status": "success", "url": f"/static/photo.jpg?t={int(time.time())}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
