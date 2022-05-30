from authentication import Login, SignUp, Logout

def initialize_routes(api):
    api.add_resource(Login, '/login')
    api.add_resource(SignUp, '/signup')
    api.add_resource(Logout, '/logout')
    