from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating the app
app = Flask(__name__)
# NOTE: NOT LIKE SQLITE MUST ALREADY HAVE MYSQL SERVER AND DATABASE CREATED (SEE createdb.py)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '450333370bd0e313582615466fe97460a0b8355a067b46738a9a4c517dfc228d'

db = SQLAlchemy(app)

# Import the routes before running the application otherwise page won't display
from routes import *

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
