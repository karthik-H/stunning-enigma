from src.repository.user_repository import UserRepository
from src.repository.user_csv_repository import UserCSVRepository
from typing import List
from src.domain.user import User
import logging
import os
from src.config.config import Config

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        csv_path = os.getenv('USER_CSV_PATH', 'data/users.csv')
        self.user_csv_repository = UserCSVRepository(csv_path)

    def get_all_users(self) -> List[User]:
        try:
            return self.user_repository.fetch_all_users()
        except Exception as e:
            logging.error(f"Service error: {e}")
            raise

    def save_users_to_csv(self, users: List[User]) -> None:
        try:
            self.user_csv_repository.save_users_to_csv(users)
        except Exception as e:
            logging.error(f"Service error saving users to CSV: {e}")
            raise
