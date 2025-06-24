from typing import List, Optional
from models.user import User

# In-memory “DB”
_users: List[User] = []

def get_users() -> List[User]:
    return _users

def get_user(user_id: int) -> Optional[User]:
    return next((u for u in _users if u.id == user_id), None)

def create_user(user: User) -> User:
    user.id = len(_users) + 1
    _users.append(user)
    return user
