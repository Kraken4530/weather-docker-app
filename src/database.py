import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base


ASYNC_DATABASE_URL = f'{os.getenv('DATABASE_URL')}'

engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)
AsyncSessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False
)
Base = declarative_base()
