from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from .config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def test_database_connection():
    try:
        engine = create_engine(settings.DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("Conexión a la base de datos exitosa.")
    except SQLAlchemyError as e:
        print("Error al conectar a la base de datos:", e)

def get_db():
    db = SessionLocal()
    try:
        test_database_connection()
        yield db
    finally:
        db.close()