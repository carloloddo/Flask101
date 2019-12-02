from app import db
from app.models.users import User

db.create_all()

guest = User(username='guest', email='guest@gmail.com', password='password')
admin = User(username='admin', email='admin@gmail.com', password='password')

db.session.add(guest)
db.session.add(admin)

db.session.commit()