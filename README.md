# Flask-with-React-POC

# Create a virtual environment
python -m venv "virtual environment name"

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

# Access data from post request
1- This is used to access form data that is submitted via an HTML form using the POST method  
    request.get_form['description']
    title = data.get('title')
2- This is used to access JSON data sent in the request body. It is typically associated with HTTP requests that have
    a Content-Type of application/json.
    data = request.get_json()
    title = data.get('title')

# Access the query parameters in flask
    http://127.0.0.1:5000/get_article_by_id/search?author_name="Jeet"&category="flask"
    author_name = request.args.get('author_name')
    category_name = request.args.get('category')
    
# How to start to work Reactjs
    npx create-react-app app_name
                or
    npm init react-app my-app

# TO run Reatjs app
npm start

# Bundles the app into static files for production.
npm run build

# Starts the test runner.
npm test

