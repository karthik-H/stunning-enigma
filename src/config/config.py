import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JSONPLACEHOLDER_API_URL = os.getenv('JSONPLACEHOLDER_API_URL')
