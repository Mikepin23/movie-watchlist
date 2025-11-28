from app import app, db

# This script will run migrations automatically on startup
with app.app_context():
    db.create_all()
    print("Database tables created.")
