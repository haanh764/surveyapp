from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.routes import initialize_routes
from flask_jwt_extended import JWTManager
from common.settings import JWT_SECRET_KEY

app = Flask(__name__)

app.config['SECRET_KEY']=JWT_SECRET_KEY

CORS(app)
api = Api(app)
jwt = JWTManager(app)

initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
