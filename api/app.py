from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from common.settings import *

app = Flask(__name__)
app.config['JWT_SECRET_KEY']= JWT_SECRET_KEY
app.config['SECURITY_PASSWORD_SALT']= SECURITY_PASSWORD_SALT
app.config['MAIL_SERVER']= MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
app.config['PROPAGATE_EXCEPTIONS'] = PROPAGATE_EXCEPTIONS
app.config['JWT_BLACKLIST_ENABLED'] = JWT_BLACKLIST_ENABLED
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = JWT_BLACKLIST_TOKEN_CHECKS
app.config["JWT_COOKIE_SECURE"] = JWT_COOKIE_SECURE
app.config['JWT_TOKEN_LOCATION'] = JWT_TOKEN_LOCATION
app.config["JWT_COOKIE_CSRF_PROTECT"] = JWT_COOKIE_CSRF_PROTECT

CORS(app)
api = Api(app)
jwt = JWTManager(app)
mail = Mail(app)
