import pathlib
basedir = pathlib.Path(__file__).parent.resolve()

# SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_ECHO=True

SQLALCHEMY_RECORD_QUERIES=True