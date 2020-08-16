from sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:1234@localhost:3306/doctrine')
