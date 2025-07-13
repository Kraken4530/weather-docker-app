from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import models
import schemas


async def get_all(db: AsyncSession):
    result = await db.execute(select(models.Weather))
    return result.scalars().all()


async def get_first(db: AsyncSession):
    result = await db.execute(select(models.Weather).limit(1))
    return result.scalars().first()


async def create(db: AsyncSession, weather: schemas.WeatherCreate):
    db_obj = models.Weather(**weather.dict())
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj
