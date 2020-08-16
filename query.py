from sqlalchemy.orm import sessionmaker
from connector import engine
from user import User
from account import Account


Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

for data in session.query(Account).order_by(Account.id):
    print(data)

session.close()
