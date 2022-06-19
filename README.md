# SurveyApp

A web application for fastly creating surveys, and get the insight from respondents via automated analysis report. 

## Structure of project:

Our application is created in form of microservices, which contains 5 services separately, including:

- `db`: mysql service for database (detail information in the next section)
- `phpmyadmin`: service for database administration
- `api`: service for application back-end (detail information in next section)
- `ui`: service for application front-end (detail information in next section)
- `nginx`: service for web server

Each of the above service is a separate docker container, and will be deployed with Docker Compose. All the services consume each others' functions via REST APIs.

Below is the structure of our repository:

```
├── api
├── db
├── docker-compose.debug.yml
├── docker-compose.yml
├── nginx
├── README.md
└── ui
```

- `/api`: contains the code for application back-end (create RESTful API)
- `/db`: contains the sql scripts for creating database
- `/nginx`: contain config for web server
- `/ui`: containes the code for application front-end
- `docker-compose.yml` - deployment configuration for each service


## How to Run:

1. Clone and cd to the repository
    
    `git clone https://github.com/haanh764/surveyapp.git`
    
    `cd surveyapp`  
    
2. Start services
    
    - run `docker-compose build` for building containers for all services
    
    - Start database services: run `docker-compose up db phpmyadmin` 
    
    - Start other services: run `docker-compose up api nginx ui`
    
    (Since when initialize api, the default admin data will be created, therefore the database service should be started already before starting api)
    
3. Server information

    Access database by `localhost:8080`
    - username: user
    - password: password123
    - database name: surveydb

   Access API by: `localhost:8000`
   
   Access Web app by: `localhost:8001`
   
   (information for port binding could be found in `docker-compose.yml`)
   
## Database

-- TODO --

## Front-end

Below is the structure of `/ui`:

```
├── README.md
├── Dockerfile
├── package.json
├── src/
  ├── api
  ├── store
  ├── router
  ├── views
  ├── components
  ├── layouts
  ├── assets
  ├── form-builder
  ├── filters
  ├── mixins
  ├── plugins
  ├── styles
  ├── util
  ├── mocks/server
  ├── App.vue
  ├── main.js
  ├── registerServiceWorker.js
├── tests/e2e/
├── .gitignore
├── .dockerignore
├── .env.development
├── .env.production
├── .browserslistrc
├── jsconfig.json
├── vue.config.js
├── .editorconfig
├── .eslintrc.js
├── babel.config.js
├── cypress.config.js
```

- `README.md` - UI-development-specific readme file providing information how to run the UI using `yarn-serve` for hot reloads, and how to run tests using `cypress`.
- `Dockerfile` - Contains the command for image api, which will be run when build the service.
- `package.json` - Contains the required dependencies; they are automatically installed when building the image ui.
- `src/` - Contains the source code 
- `tests/e2e/` - 
- `.gitignore` - 
- `.dockerignore` - 
- `.env.development` - 
- `.env.production` - 
- `.browserslistrc` - 
- `jsconfig.json` - 
- `vue.config.js` - 
- `.editorconfig` - 
- `.eslintrc.js` - 
- `babel.config.js` - 
- `cypress.config.js` - 

## Back-end

Below is the structure of `/api`:

```
├── app.ini
├── app.py
├── common
├── database
├── Dockerfile
├── __init__.py
├── models
├── postman_json
├── __pycache__
├── requirements.txt
├── resources
└── run.py
```

- `Dockerfile` - contains the command for image api, which will be run when build the service
- `app.ini` - contains config for uWSGI server for serving Flask application, in conjunction with web server which is nginx
- `app.py` - initialize Flask application with configuration
- `run.py` - run Flask application
- `requirements.txt` - contains the required libraries, when service api is built, the requirements in this file will be installed.
- `/database` - contains class and configurations for Database Connector. We use the `SQLAlchemy` as the Object Relational Mapping (ORM) for database connector
- `/common` - contains the common helper classes that will be used in multiple places in api, including all default settings for configuration in back-end (file `settings.py`); helper functions for user and authentication (file `authentication_helper.py`); some helper functions for creating dashboard (in `utils.py` - create charts, and `queries.py` - query responses data for analysis dashboard)
- `models` - contains the Declarative Mappings that map each Python class to its corresponding table in database. The Declarative Mapping classes are inherited from Declarative Base from SQLAlchemy. Below is an example of how the `User` class is constructed using declarative mapping:

    ```
    from sqlalchemy import Column, Integer, String, Boolean
    from sqlalchemy.orm import relationship
    from database.db_config import Base, session

    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True, index=True)
        email = Column(String(100), nullable=False)
        password = Column(String(100), nullable=False)
        isActivated = Column(Boolean, nullable=False, default=False)
        isBlocked = Column(Boolean, nullable=False, default=False)
        surveys = relationship("Survey", back_populates="users", cascade="all, delete-orphan")
    ```


- `resources` - contains class for each API. We use Flask-Restful for creating RESTful API. Each class is extended from class `Resources()` from Flask-Restful, which represents an abstract of RESTful resource, and then expose methods for each supported HTTP method. Below is an example of resource class for User Login API:

    ```
    class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.find_by_email(data['email'])
        if user and user.check_password(data['password']):
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=user.id, expires_delta=expires, additional_claims={'is_admin': False})
            response = jsonify({'message': 'Logged in as {}. Access token is {}'.format(user.email, access_token)})
            set_access_cookies(response, access_token)
            response.status_code = 200
            return response
        return {'message': 'Invalid username or password'}, 401
    ```
    
        
    In `/resources/routes.py`, the route for each api is created using `api.add_resource()`, for example: `api.add_resource(Login, '/api/authentication/login')`
    

- `postman_json` - contains the `.json` scripts for testing APIs using postman
