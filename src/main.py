from fastapi import FastAPI
from routers.weather import router, lifespan

app = FastAPI(lifespan=lifespan)
app.include_router(router)
