from app.models.user import User

# Dummy data store
_users = {
    1: User(1, "Alice"),
    2: User(2, "Bob")
}

def get_user_by_id(user_id):
    return _users.get(user_id)

def get_all_users():
    return list(_users.values())
