from package import app, db
from package import routes

# Register blueprints
app.register_blueprint(routes.article_bp, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)
