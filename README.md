# SurveyApp

Structure of project:
- /api: contains the code for backend (create RESTful API)
- /db: contains the code for creating database
- /nginx: contain config for webserver (dont edit the config file)
- /ui: containes the code for vuejs frontend
    - src/components: contains components of frontend
    - src/router: control routing of website
    - src/views: contains code for view of website

Guidlines:

1. Clone and cd to the repository
2. run `docker-compose up` (or `docker-compose build` for building the containers, and then `docker-compose up` to start the services)
3. Access database by `localhost:8080`
    - username: user
    - password: password123
    - database name: surveydb

   Access API by: `localhost:8000`
   Access Web app by: `localhost:8001`
   