from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE=declarative_base()
MD=MetaData()

SQLALCHEMY_DTABASE_URL = "sqlite:///./Blog.db"
#"mssql+pyodbc://:@GAVUTHAM/Blog.db"
# "sqlite:///./Blog.db"
engine = create_engine(SQLALCHEMY_DTABASE_URL, connect_args={"check_same_thread": False})
# engine = create_engine(SQLALCHEMY_DTABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    MD.create_all(bind=engine)
    print('db created success')
except:
    print('db not created')