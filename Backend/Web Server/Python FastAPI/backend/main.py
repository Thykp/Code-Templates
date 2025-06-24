from fastapi import FastAPI
from fastapi.routing import APIRouter
from routers.user_router import router as user_router

app = FastAPI(title="My FastAPI App")

app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return {"message": "FastAPI App is running!"}
