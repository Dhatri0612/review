from fastapi import FastAPI
from project.routes.routes import router

app=FastAPI()
app.include_router(router)
