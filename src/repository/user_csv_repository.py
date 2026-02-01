import csv
import logging
from typing import List
from src.domain.user import User
import os
import json

class UserCSVRepository:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)

    def save_users_to_csv(self, users: List[User]) -> None:
        try:
            with open(self.csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'id', 'name', 'username', 'email', 'phone', 'website', 'address', 'company'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for user in users:
                    writer.writerow({
                        'id': user.id,
                        'name': user.name,
                        'username': user.username,
                        'email': user.email,
                        'phone': user.phone,
                        'website': user.website,
                        'address': json.dumps(user.address, ensure_ascii=False),
                        'company': json.dumps(user.company, ensure_ascii=False)
                    })
            logging.info(f"Successfully saved {len(users)} users to CSV at {self.csv_path}")
        except Exception as e:
            logging.error(f"Error saving users to CSV: {e}")
            raise
