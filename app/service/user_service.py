from sqlalchemy.orm import Session

from app.repository.user_repository import UserRepository
from app.model.user import User


class UserService:

    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, db: Session, user: User):
        return self.repo.create(db, user)

    def get_user(self, db: Session, user_id: int):
        return self.repo.get_by_id(db, user_id)

    def get_by_username(self, db: Session, username: str):
        return self.repo.get_by_username(db, username)

    def list_users(self, db: Session):
        return self.repo.get_all(db)

    def update_user(self, db: Session, user: User):
        return self.repo.update(db, user)

    def delete_user(self, db: Session, user: User):
        return self.repo.delete(db, user)