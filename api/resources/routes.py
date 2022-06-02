from .authentication import Login, SignUp, Logout
from .view import Home

def initialize_routes(api):
    api.add_resource(Home, '/api/home')

    api.add_resource(Login, '/api/authentication/login')
    api.add_resource(SignUp, '/api/authentication/signup')
    api.add_resource(Logout, '/api/authentication/logout')