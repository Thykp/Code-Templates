class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def to_dict(self):
        return {"user_id": self.user_id, "username": self.username}
