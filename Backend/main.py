# main.py
from package import create_app
from package.routes.articles_route import article_bp

# Register blueprints
app = create_app()
app.register_blueprint(article_bp)


def close_db_connection(db):
    if db:
        db.close()


if __name__ == "__main__":
    app.run(debug=True)
