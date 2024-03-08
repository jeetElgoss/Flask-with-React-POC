import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = os.getenv("DEBUG")
    DATABASE_URL = os.getenv("DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")


