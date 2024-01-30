from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

POSTGRES_DB_USER = 'counter_user'
POSTGRES_DB_PASSWORD = 'ThePassw0rD'
POSTGRES_DB_HOST = '127.0.0.1'
POSTGRES_DB_PORT = '5431'
POSTGRES_DB_NAME = 'counter_db'

DATABASE_URL = f"postgresql://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class CounterTable(Base):
    __tablename__ = "counter_table"
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0)

def init_db():
    Base.metadata.create_all(bind=engine)

def increment_counter(db, count):
    try:
        counter = db.query(CounterTable).first()
        if counter:
            counter.count += count
        else:
            counter = CounterTable(count=count)
            db.add(counter)
        db.commit()
        return counter.count
    except SQLAlchemyError as e:
        db.rollback()
        raise e
