from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

db_url = os.getenv("postgresql://fastapi_db_93m1_user:tFqfEoZCAeFE4JaCaMfJuJ3GlgjOag0g@dpg-d6668mi4d50c73b4he3g-a.oregon-postgres.render.com/fastapi_db_93m1")
engine = create_engine(db_url)
# session is cycle of server to database or to client or vice versa
session = sessionmaker(autocommit=False, autoflush=False, bind=engine) 