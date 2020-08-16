from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base =  declarative_base()

class Account(Base):
        __tablename__ = 'tbl_account'

        id = Column(Integer, primary_key=True)
        state_name = Column(String)
        account_name = Column(String)

        def __repr__(self):
             return "<Account(state_name='%s', account_name='%s')>" % (self.state_name, self.account_name)
