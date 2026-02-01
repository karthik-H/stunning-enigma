import logging
from src.controller.user_controller import display_users

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
    display_users()
