from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for declarative class definitions
Base = declarative_base()

#  Define he Password class
class Password(Base):
    # The name of the table in the database
    __tablename__ = 'passwords'
    # Define columns in the table
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(String, nullable=False)
    service = Column(String, nullable=False)
    password = Column(String, nullable=False)

# Create an SQLite database engine
engine = create_engine('sqlite:///passwords.db')

#  Create the tables in the database
Base.metadata.create_all(engine)

#  Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()