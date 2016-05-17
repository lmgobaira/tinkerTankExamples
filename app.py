"""
Tinker Tank V : Python Meetup
Description : Simple Flask app + with GPIO usage
Contact: lgobaira@gmail.com
MAY 2016

"""

# Import necessary external libraries
import time

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
# The @symbol denotes a decorator. Decorators make complex things easier.
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
    GPIO.output(led_pin, 0)
    return "Light is Off"


@app.route("/blink/")
def led_blink():
    """
    Blink little light blink!
    :return:
    """

    # Blink 10 times with 1 second pause between state changes
    # ***Caution**** : Long running process should be executed ASYNC (Queue, thread, Celery, etc)
    count = 0
    while count < 10:
        GPIO.output(led_pin, 0)
        time.sleep(1)
        GPIO.output(led_pin, 1)
        time.sleep(1)
        count += 1
    return "It was blinking. Whoa!"


@app.route("/ipinfo/")
def ip_info():
    """
    Makes a GET request using requests library to http://jsonip.com/ then dumps response
    :return:
    """
    # Make a request to external API (also try http://www.timeapi.org/utc/now, or any other  REST API endpoint)
    r = requests.get('http://jsonip.com/')
    return r.text


@app.route("/")
def hello():
    """
    Hello World!
    :return:
    """
    return "<h1> Tinker Tank V: Python</h1><p>Hola Amigos</p>"


# Some simple 404 error Catching
@app.errorhandler(404)
def page_not_found(error):
    """
    Prints error message on screen using .format method and string substitution.

    :param error:
    :return:
    """
    return "<h1>Doh..</h1> {}".format(error)


# This block of code executes when the program is called directly (not via interpreter)
if __name__ == "__main__":
    # Turns on debug mode
    app.debug = True
    # Starts app and binds to all interfaces ( ie makes app available on the network)
    app.run(host="0.0.0.0")
    GPIO.cleanup()
