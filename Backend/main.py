# main.py
from package import create_app
from package.routes.articles_route import article_bp

# Register blueprints
app = create_app()
app.register_blueprint(article_bp)

if __name__ == "__main__":
    app.run(debug=True)