from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from . import settings

Base = automap_base()

CONNECTION_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}"\
                 f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"

engine = create_engine(CONNECTION_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.prepare(engine, reflect=True)
