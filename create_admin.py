from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    admin = User.query.filter_by(
        email="admin@example.com"
    ).first()

    if admin:
        admin.role = "admin"
        admin.password = generate_password_hash("admin123")
    else:
        admin = User(
            name="Admin",
            email="admin@example.com",
            password=generate_password_hash("admin123"),
            role="admin"
        )
        db.session.add(admin)

    db.session.commit()

    print("Admin login ready!")
    print("Email: admin@example.com")
    print("Password: admin123")