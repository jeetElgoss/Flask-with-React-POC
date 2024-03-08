# Flask-with-React-POC

# Create db using migrate command 
1- $env:FLASK_APP = "package"(package means where your __init__.py is, which is containing flask app object.)
2- flask db init
3- flask db migrate -m "initial message"
4- flask db upgrade
        or 
   flask db downgrade