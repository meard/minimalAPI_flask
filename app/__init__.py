from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = '34gHVSIBV4hGbs8ydasbvsjdf'
app.debug = True

from app import routes