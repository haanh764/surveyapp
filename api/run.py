from app import app, api
from resources.routes import initialize_routes
from common.utils import init_admin_default

initialize_routes(api)
init_admin_default()

if __name__ == "__main__":
    app.run(debug=True)
