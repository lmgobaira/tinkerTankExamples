"""
Tinker Tank V : Python Meetup
Description : Simple Flask app + with GPIO usage
Contact: lgobaira@gmail.com
MAY 2016

"""

# Import necessary external libraries
import RPi.GPIO as GPIO
import requests
from flask import Flask

# Lets create an instance of a Flask app
app = Flask(__name__)

# Setup the GPIO pins
led_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_pin, GPIO.OUT)


# Defining flask routes
@app.route("/on/")
def led_on():
    """
    Turn on LED pin 4 to ON any request to http://<server>/on
    :return:
    """
    GPIO.output(led_pin, 1)
    return "Light is On"


@app.route("/off/")
def led_off():
    """
    Turn on LED pin 4 to ON any request to http://<server>/off
    :return:
    """
    GPIO.output(led_pin, 1)
    return "Light is Off"


@app.route("/ipinfo/")
def ip_info():
    """
    Makes a GET request using requests library to http://jsonip.com/ then dumps response
    :return:
    """
    # Make a request to external API
    r = requests.get('http://jsonip.com/')
    return r.text


@app.route("/")
def hello():
    """
    Hello World!
    :return:
    """
    return "<h1> Tinker Tank V: Python</h1><p>Hola Amigos</p>"


# Some simple error Catching
@app.errorhandler(404)
def page_not_found(error):
    return "Doh.. {}".format(error)


# This block of code executes when the program is called directly (i.e. not via interpreter)
if __name__ == "__main__":
    # Turns on debug mode
    app.debug = True
    # Starts app and binds to all interfaces ( ie makes app available on the network)
    app.run(host="0.0.0.0")
