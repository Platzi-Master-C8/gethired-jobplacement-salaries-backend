from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

Base = automap_base()

CONNECTION_URL = "postgresql://postgres:postgres@db/salaries"

engine = create_engine(CONNECTION_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.prepare(engine, reflect=True)
