from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
db = Session()