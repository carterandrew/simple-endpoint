import logging

from flask import Flask, jsonify, request
app = Flask(__name__)

_LOG_FILENAME = 'debug.log'
_LOG_FORMAT = '[%(asctime)s] %(message)s'
_PLAIN_HTML_RESPONSE = '<p>Hello, World</p>'
_JSON_RESPONSE = {'message': 'Good morning'}


def _accepts_json():
    if ('Accept' in request.headers
        and request.headers['Accept'] == 'application/json'):
        return True
    return False


@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.debug(request.url)
    if request.method == 'GET' and _accepts_json():
        return jsonify(_JSON_RESPONSE)
    return _PLAIN_HTML_RESPONSE
        
        
if __name__ == '__main__':
    handler = logging.FileHandler(_LOG_FILENAME)
    formatter = logging.Formatter(_LOG_FORMAT)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)
    app.run() 