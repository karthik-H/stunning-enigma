from src.repository.user_repository import UserRepository
from typing import List
from src.domain.user import User
import logging

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self) -> List[User]:
        try:
            return self.user_repository.fetch_all_users()
        except Exception as e:
            logging.error(f"Service error: {e}")
            raise
