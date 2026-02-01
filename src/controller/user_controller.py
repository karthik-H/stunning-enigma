from src.service.user_service import UserService
import logging

def display_users():
    user_service = UserService()
    try:
        users = user_service.get_all_users()
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Username: {user.username}, Email: {user.email}, Phone: {user.phone}, Website: {user.website}")
    except Exception as e:
        logging.error(f"Controller error: {e}")
        print("Failed to retrieve users.")
