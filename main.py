from random import choice

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
# from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.staticfiles import StaticFiles

from apps.routers import api, auth
from apps import models
from database import engine, get_db

from faker import Faker

app = FastAPI()

app.mount("/static", StaticFiles(directory='static'), name='static')
# app.mount("/media", StaticFiles(directory='media'), name='media')


@app.on_event("startup")
def startup():
    # app.add_middleware(AuthenticationMiddleware())  # Add the middleware with your verification method to the whole application
    pass
    db = next(get_db())
    # models.Base.metadata.drop_all(engine)
    models.Base.metadata.create_all(engine)
    # p1 = models.Position(name='Full Developer')
    # p2 = models.Position(name='Frontend')
    # positions = [p2, p1]
    # db.add_all(positions)
    # db.commit()


app.include_router(api)
app.include_router(auth)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)