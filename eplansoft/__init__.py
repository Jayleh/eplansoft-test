from flask import Flask

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'eplansoft/uploads/'

from eplansoft import routes
