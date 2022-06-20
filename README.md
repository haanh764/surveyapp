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

Below is the structure of `/db`:

```
├── create_db.sql
├── dump_mockup_data.sql
```

- `create_db.sql` - File which contains queries for creation of all the database tables and relations between them.
- `dump_mockup_data.sql` - Contains queries for inserting mockup data used for testing into database.

`create_db.sql` initially drops all the tables if they exist, so when recreating db, to allow the application to run, it is necessary to run `dump_mockup_data.sql` to have some data in database.
All actual database queries are executed in `back-end` using `sqlalchemy ORM` models.

Below is an example of database query using `sqlalchemy ORM`.

```
session.query(Admin).filter_by(email=email).first()
```

In this example `Admin` is an ORM class derived from `sqlalchemy.ext.declarative.declarative_base`. Below is a part of the `Admin` declaration:

```
class Admin(Base):
	__tablename__ = 'administrators'
	id = Column(Integer, primary_key=True, index=True)
	email = Column(String(100), nullable=False)
	password = Column(String(100), nullable=False)
	.
	.
	.
```

## Front-end

Below is the structure of `/ui`:

```
├── README.md
├── Dockerfile
├── package.json
├── src/
├── tests/e2e/
├── .env.development
├── .env.production
├── jsconfig.json
├── vue.config.js
├── .eslintrc.js
├── babel.config.js
├── cypress.config.js
```

- `README.md` - UI-development-specific readme file providing information how to run the UI using `yarn-serve` for hot reloads, and how to run tests using `cypress`.
- `Dockerfile` - Contains the command for image api, which will be run when build the service.
- `package.json` - Contains the required dependencies; they are automatically installed when building the image ui.
- `src/` - Contains the main source code for the UI. More details below.
- `tests/e2e/` - Contains the configuration and test scripts using cypress.
- `.env.development` - Contains global environment variables for Development.
- `.env.production` - Contains global environment variables for Production.
- `jsconfig.json` - Settings for the JavaScript's root files and features.
- `vue.config.js` - Settings for Vue.js's system.
- `.eslintrc.js` - Settings for `eslint`, a tool for automatically detecting problematic patterns in the JavaScript code.
- `babel.config.js` - Settings for `babel`, a tool for ensuring backwards-compatibility with browsers with older JavaScript engines.
- `cypress.config.js` - Settings for `cypress`, the end-to-end testing tool used for requirement testing in this project.

Below is the structure of `/ui/src`, which contains the main source code:

```
├── src/
  ├── api/
  ├── store/
  ├── router/
  ├── views/
    ├── admin/
	├── user/
	├── general/
	├── PageNotFoundView.vue
  ├── components/
  ├── layouts/
  ├── assets/
  ├── form-builder/
  ├── filters/
  ├── mixins/
  ├── plugins/
  ├── styles/
  ├── util/
  ├── mocks/
  ├── App.vue
  ├── main.js
  ├── registerServiceWorker.js
```

- `api` - Contains code for functions that call the APIs provided by Back-End. These functions are utilizing `axios` to make requests and can be found in `index.js`, while `config.js` contains axios settings and `url.js` contains the list of URLs to the APIs. Below is an example of how the function to call the API to log the user in was defined in `api/index.js`:

  ```
  const axios = require("axios");

  axios.defaults.baseURL = baseURL; // defaults to 'http://localhost:8000/api/ in development mode

  const USER_LOGIN_URL = "authentication/login";
  export const userLogin = (data) => {
      return axios.post(USER_LOGIN_URL, data);
  };

  ```

  Then, the function can be called in the `LoginView.vue` component as such:

  ```
  <script>
  import { userLogin } from "@api";

  export default {
      methods: {
          onFormSubmit() {
              this.isLoading = true;
              const apiData = {email: "test@test.com", password: "1234567890" };
              userLogin(apiData).then((response)=> {
                  // do something with the response
              }).catch((error)=> {
                  // do something on error
              })
          }
      }
  }
  </script>
  ```

- `store` - Contains code for centralized state management for Vue.js, and also for writing and removing client-side data to/from cookies. The store is managed by Vuex library. The store contains 2 modules for easier state management, namely the `app` and `user` module. The `user` module contains user data, while the `app` module contains data needed for UI management, such as the visibility and size of the sidebar.

  ```
  import Vue from "vue";
  import Vuex from "vuex";
  import * as modules from "./modules";

  const store = new Vuex.Store({
  modules,
  });

  export default store;

  ```

  The store is later imported in `main.js` and initialized as part of Vue environment.

  ```
  new Vue({
      store,
      render: (h) => h(App)
  }).$mount("#app");

  ```

- `router` - Contains code for routing rules for Vue.js. In other words, the code here decides which page (view) to serve, sets what layout to use, and also provides some navigation guards to prevent unauthorized access to certain pages (views). Below is an example of how the route for the landing page was created in `router/index.js`:

  ```
  import Vue from "vue";
  import Router from "vue-router";

  Vue.use(Router);

  const router = new Router({
  mode: NODE_ENV == "development" ? "history" : "hash",
  base: process.env.BASE_URL,
  routes: [
      {
      path: "/",
      name: "general-landing",
      component: () =>
          import(
          /* webpackChunkName: "general-landing" */ "@views/general/landing/LandingView.vue"
          )
      }]
  });

  export default router.
  ```

  The `router` is later imported in `main.js` and initialized as part of Vue environment.

  ```
  new Vue({
      router,
      render: (h) => h(App)
  }).$mount("#app");

  ```

- `layouts` - Contains code for controlling page layout structures and their components, like Drawer and Footer.
- `views` - Contains code for main pages of the web app. A user navigates between these views with the router.
- `views/admin` - Contains code for admin pages.
- `views/user` - Contains code for user pages.
- `views/general` - Contains code for general pages, which are pages that can be accessed without logging-in.
- `views/PageNotFoundView.vue` - Contains code for the 404 page, which is shown when the resource requested by the client's browser is not available.
- `components` - Contains code for re-usable components like Modal, ContentCard, and BottomSheet. These components are mainly used by the views.
- `form-builder` - Contains code for building a dynamic form, which is mainly used when a user creates/edits a survey, as well as for generating the dynamic form on the survey response page.
- `assets` - Contains static images and json files that can be loaded in any view, component, or layout element.
- `mixins` - Contains code for Vue.js's mixins, which are helper objects that can provide utility methods to components.
- `plugins` - Contains settings for the Vue.js plugins.
- `styles` - Contains global scss and JavaScript styling, including theme colors and typography.
- `filters` - Contains utility filter functions for Vue like capitalizing strings and formatting a date to a standard format.
- `util` - Contains utility functions like formatting a date to a standard format, checking if today is after a given date, and copying text to clipboard.
- `mocks` - Contains code for making mock APIs that can be used for development purposes.
- `App.vue` - Contains the root Vue object. Executing this file runs the UI app.
- `main.js` - Contains code for initializing the root into an element on a page, and also for connecting the UI app with plugins.
- `registerServiceWorker.js` - Generated by the Vue PWA plugin, it runs a service in the background for caching network requests.

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
