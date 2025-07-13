from pydantic import BaseModel


class WeatherCreate(BaseModel):
    city: str
    temperature: int


class WeatherOut(BaseModel):
    id: int
    city: str
    temperature: int

    class Config:
        orm_mode = True
