from sqlmodel import JSON, Column, SQLModel, Field
from typing import List

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    email: str = Field(unique=True)
    experience_years: int | None = None
    hourly_rate: float | None = None
    city: str | None = None
    country: str | None = None
    remote: bool | None = None
    skills: List[str] = Field(sa_column=Column(JSON))
    