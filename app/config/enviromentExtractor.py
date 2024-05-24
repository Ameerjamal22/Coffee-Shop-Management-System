from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_SERVER_USERNAME = os.getenv("DATABASE_SERVER_USERNAME")
DATABASE_SERVER_PASSWORD = os.getenv("DATABASE_SERVER_PASSWORD")
