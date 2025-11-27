from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from config import Config
from extensions import bcrypt, db
from flask_login import LoginManager
from controllers.auth_controller import handle_register, handle_login
from dotenv import load_dotenv
from flask_migrate import Migrate

# Allow .env variables to be loaded
load_dotenv()

# Create Flask application instance
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)


# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Initialize CSRF protection
csrf = CSRFProtect(app)


# Import models to register them with SQLAlchemy
from models.user import User
from models.movie import Movie

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Create Bcrypt instance once
bcrypt.init_app(app)

# Register Blueprints
from routes.auth_routes import auth_bp
app.register_blueprint(auth_bp)
from routes.movie_routes import movie_bp
app.register_blueprint(movie_bp)

# Run the app
if __name__ == '__main__':
    app.run()