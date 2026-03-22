from flask import Flask, render_template
import random  # Replace with sensor libraries later
import time
import smbus2
import bme280
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

# BME280 sensor address (default address)
address = 0x76

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)

app = Flask(__name__)

def get_sensor_data():
    """
    Galaxy Explorers: Replace these random numbers with your 
    actual Raspberry Pi sensor reading code!
    """
    data = bme280.sample(bus, address, calibration_params)

    # Extract temperature, pressure, and humidity
    temperature_celsius = data.temperature
    pressure = data.pressure
    humidity = data.humidity
    return {
        "temp": temperature_celsius,
        "humidity": humidity,
        "pressure": pressure
    }

@app.route('/')
def index():
    data = get_sensor_data()
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
