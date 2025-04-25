from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Annotated

import models
from database import sessionLocal, engine
from models import Todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get('/')
async def read_all(db : db_dependency):
    return db.query(Todos).all()