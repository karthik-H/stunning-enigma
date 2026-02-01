import requests
from typing import List
from src.config.config import Config
from src.domain.user import User
import logging

class UserRepository:
    def __init__(self):
        self.api_url = Config.JSONPLACEHOLDER_API_URL
        self.endpoint = f"{self.api_url}/users"

    def fetch_all_users(self) -> List[User]:
        try:
            response = requests.get(self.endpoint, timeout=10)
            response.raise_for_status()
            users_data = response.json()
            return [User.from_dict(user) for user in users_data]
        except requests.RequestException as e:
            logging.error(f"Error fetching users from API: {e}")
            raise
