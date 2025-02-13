from app import db, app

with app.app_context():
    db.create_all()
    print("Database created!")


# Run in env (env\Scripts\activate) using python create_db.py