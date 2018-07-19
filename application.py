from flask import Flask
from flask.ext.migrate import Migrate
import os, sys
from flask_cors import CORS
from flask_compress import Compress

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

application = Flask(__name__)

application.config.from_object('settings')

CORS(application)
Compress(application)

from general.api import *

if __name__ == "__main__":
    application.debug = application.config['DEBUG']
    application.run(host='0.0.0.0')
