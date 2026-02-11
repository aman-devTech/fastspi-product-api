from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)
# session is cycle of server to database or to client or vice versa
session = sessionmaker(autocommit=False, autoflush=False, bind=engine) 