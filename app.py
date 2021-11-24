from flask import Flask
from configparser import ConfigParser
# create a ConfigParser class instance
conf_obj=ConfigParser()

# read all information from config file
conf_obj.read('flask_config.ini')
app_info=conf_obj["APPINFO"]
app = Flask(__name__)
app.env=app_info.get("env")
app.secret_key=app_info.get('secret_key')
app.debug=bool(app_info.get('debug'))