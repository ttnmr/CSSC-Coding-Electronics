  GNU nano 8.4                                                    app.py
from flask import Flask, render_template, jsonify
from picamera2 import Picamera2
import time

app = Flask(__name__)

# initialize camera
picam2 = Picamera2()
picam2.start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/capture")
def capture():
    filename = "static/photo.jpg"
    time.sleep(1)
    picam2.capture_file(filename)
    return jsonify({"status": "photo taken", "file": filename})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

