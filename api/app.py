from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from common.settings import JWT_SECRET_KEY, SECURITY_PASSWORD_SALT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_SERVER

app = Flask(__name__)
app.config['JWT_SECRET_KEY']=JWT_SECRET_KEY
app.config['SECURITY_PASSWORD_SALT']=SECURITY_PASSWORD_SALT
app.config['MAIL_SERVER']=MAIL_SERVER
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

CORS(app)
api = Api(app)
jwt = JWTManager(app)
mail = Mail(app)

