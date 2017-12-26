from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from settings import settings

db_url = 'postgresql+psycopg2://{user}:{password}@{host}:5432/{dbname}'.format(
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    host=settings.POSTGRES_HOST,
    dbname=settings.POSTGRES_DB
)
engine = create_engine(db_url, pool_size=20, max_overflow=0)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

session = Session()
