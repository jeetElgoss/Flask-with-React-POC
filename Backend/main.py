# main.py
from package import create_app
from package.routes.articles_route import article_bp

# Register blueprints
app = create_app()
app.register_blueprint(article_bp)

"""This is primary route, which will run when user visit http://127.0.0.1:5000/"""


@app.route("/")
def index():
    return "<center></h2>Welcome to my platform.</h2></center>"


if __name__ == "__main__":
    app.run(debug=True)
