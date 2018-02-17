**API WITH PYTHON Flask-Restful**

###
# This api is using flask with postgres sql

## Run it in virtual environment
```
source venv/bin/activate
```

## Installation
```
pip install Flask
pip install Flask-RESTful
Pip install Flask-JWT
pip install Flask-SQLAlchemy
pip install psycopg2
pip install Flask-Cors
```

## Description
### Implementation with flask and flask-restfull with auth using JWT token.

## Run the project
```
python app.py
```

## All the database models are defined under models and we use sqlalchemy for our database
## all the route endpoints are defined under resources which by conventions follow to take models from models directory
## we are using uwsgi server runner to start our application and the file being responsible for starting the web app in production is run.py and on development is app.py
## you can generate the requirement by reading the file requirements.txt
