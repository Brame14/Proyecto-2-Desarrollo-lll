from app.repository.user_repository import UserRepository


class AuthService:

    def __init__(self):
        self.repository = UserRepository()

    def login(self, username, password):

        users = self.repository.get_users()

        for user in users:
            if user["username"] == username and user["password"] == password:
                return True

        return False