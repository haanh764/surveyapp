from app import app, api
from resources.routes import initialize_routes

initialize_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
