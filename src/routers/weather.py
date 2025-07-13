from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

import crud
import schemas
import models
from database import AsyncSessionLocal, engine, Base

router = APIRouter()


@asynccontextmanager
async def lifespan(app):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as db:
        first = await crud.get_first(db)
        if not first:
            await crud.create(db, schemas.WeatherCreate(city="London", temperature=20))
    yield


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


@router.get('/ping', response_class=HTMLResponse)
async def ping():
    return '<h1>PONG</h1>'


@router.get('/health')
async def health():
    return JSONResponse(content={'status': 'HEALTHY'})


@router.get('/list', response_class=HTMLResponse)
async def list_weather(db: AsyncSession = Depends(get_db)):
    entries = await crud.get_all(db)
    html = '<h1>Weather</h1><ul>'
    for e in entries:
        html += f'<li>{e.city}: {e.temperature}°C</li>'
    html += '</ul>'
    return html


@router.post('/add')
async def add_weather(payload: schemas.WeatherCreate, db: AsyncSession = Depends(get_db)):
    new = await crud.create(db, payload)
    return new
