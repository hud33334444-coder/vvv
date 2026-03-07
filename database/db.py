import os
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from dotenv import load_dotenv

from database.models import Base

load_dotenv()

engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True)  # type: ignore
session = async_sessionmaker(engine)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
