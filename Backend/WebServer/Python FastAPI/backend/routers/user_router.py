from typing import List
from fastapi import APIRouter
from models.user import User
from controllers.user_controller import UserController

router = APIRouter()

@router.get("/", response_model=List[User])
def list_users():
    return UserController.list_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    return UserController.retrieve_user(user_id)

@router.post("/", response_model=User, status_code=201)
def create_user(user: User):
    return UserController.new_user(user)
