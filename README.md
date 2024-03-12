# Flask-with-React-POC

# Create a virtual environment
pyhton -m venv "virtual environment name"

# To update virtual environment
pip install -r requirements.txt --upgrade

# Create db using migrate command 
1- $env:FLASK_APP = "package"(package means where your __init__.py is, which is containing flask app object.)
2- flask db init
3- flask db migrate -m "initial message"
4- flask db upgrade
        or 
   flask db downgrade

# To work with marshmallow-sqlalchemy
pip install flask_sqlalchemy
pip install flask_marshmallow
pip install flask_migrate
pip install marshmallow-sqlalchemy

# Add git ignore 
touch .gitignore
