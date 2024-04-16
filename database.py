from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQL_URL = "sqlite:///fast.db"

engine = create_engine(SQL_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()