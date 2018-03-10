import json
import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask, jsonify, request, redirect, abort, make_response

DEBUG=True

# SETUP INITIAL APP
flask_app = Flask(__name__, static_url_path='/static')

@flask_app.route('/')
def index():
    return flask_app.send_static_file('index.html')

@flask_app.route('/login', methods=['POST'])
def fake_login():
    data = request.values.to_dict()
    flask_app.logger.info('hi there, someone tried to login')
    flask_app.logger.info(str(data))
    return flask_app.send_static_file('index.html')

def run():
    flask_app.run(host='0.0.0.0', port=8081, debug=DEBUG)

if __name__ == '__main__':
    if not DEBUG:
        print('Setting up logging...')
        fmt = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        logging.basicConfig(stream=sys.stdout, level=log_level, format=fmt)
        # Make a new log handler that uses STDOUT
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(fmt))
        handler.setLevel(log_level)
        # Remove the Flask default handlers and use our own
        handler_list = list(flask_app.logger.handlers)
        for log_handler in handler_list:
            flask_app.logger.removeHandler(log_handler)
        flask_app.logger.addHandler(handler)
        flask_app.logger.setLevel(log_level)
        flask_app.logger.info('Logging handler established')
    run()
