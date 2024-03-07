from package import app,db
from Backend.package import routes

# Register blueprints
app.register_blueprint(routes.article_bp, url_prefix='/')

import secrets

secret_key = secrets.token_hex(16)
print(secret_key)


if __name__ == "__main__":
    app.run(debug=True)
