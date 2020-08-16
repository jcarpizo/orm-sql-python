
from sqlalchemy.orm import sessionmaker
from user import User
from connector import engine


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)
