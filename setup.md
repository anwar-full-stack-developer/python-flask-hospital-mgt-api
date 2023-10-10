## Setting up Django REST framework

Create a virtual environment to isolate dependencies, however, this is optional. 

 Run the command `python -m venv flask_env` from inside your projects folder to create the virtual environment. Then, run `source ./flask_env/bin/activate` (Linux/Mac) to turn it on.
 In windows run `.\flask_env\bin\activate` (Windows) to turn it on.

## Navigate to an empty folder in your terminal and install Flask framework in your project with the commands below:

`pip install connexion flask flask_sqlalchemy  flask_marshmallow flask_restful`

## or load from file

`pip install -r requirements.txt`


## initilize the database.

`python init_db.py`

### or 

`python app.py`

## Run Server

`flask run --port 8000 --debug --reload`