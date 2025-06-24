from typing import List
from fastapi import HTTPException
from models.user import User
from services.user_service import get_users, get_user, create_user

class UserController:
    @staticmethod
    def list_users() -> List[User]:
        return get_users()

    @staticmethod
    def retrieve_user(user_id: int) -> User:
        user = get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def new_user(user: User) -> User:
        return create_user(user)
