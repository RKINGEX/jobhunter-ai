from fastapi import FastAPI, Depends
from models import User  
from database import create_db_and_tables, get_session
from sqlmodel import Session

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/profile")
def create_profile(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

create_db_and_tables()
