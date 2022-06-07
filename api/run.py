from app import app, api
from resources.routes import initialize_routes
from models.admin import Admin

initialize_routes(api)
Admin.init_admin_default()

if __name__ == "__main__":
    app.run(debug=True)
