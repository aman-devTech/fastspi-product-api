from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:password@localhost:5432/fastAPI_beginner"
engine = create_engine(db_url)
# session is cycle of server to database or to client or vice versa
session = sessionmaker(autocommit=False, autoflush=False, bind=engine) 