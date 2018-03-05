# Flask microframework (Webserver routing and associated tools)
from flask import Flask, render_template, flash, redirect, request, Response, session, url_for, jsonify
from flask_session import Session

# Other import modules
import os
import json
from passlib.hash import bcrypt
from datetime import datetime

# Object-Relational-Mapper (ORM) objects representing entities/relations
from orm_classes.tenant import Tenant
from orm_classes.landlord import Landlord
from orm_classes.property import Property

# Setup app object and configure application
app = Flask(__name__)

if os.environ['ENV_TYPE'] == 'LOCAL':
    # If local environment, import configparser module and parse local config file
    import configparser

    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'config.ini')
    config = configparser.ConfigParser()
    config.read(filename)

    local = config['LOCAL']
    # Pull database variables
    DB_HOST = local['DB_HOST']
    DB_USER = local['DB_USER']
    DB_PASSWORD = local['DB_PASSWORD']
    DB_NAME = local['DB_NAME']
else:
    # If environment is production server, parse relevant system environment variables
    DB_HOST = os.environ['DB_HOST']
    DB_USER = os.environ['DB_USER']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_NAME = os.environ['DB_NAME']

# Application Routing
# 1) Index
@app.route('/')
def index():

    test_list = [1, 2, "hello", 4, "goodbye"]

    return render_template('test.html', test_list1=test_list)

d
if __name__ == '__main__':
    app.run()
