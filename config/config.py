import os

from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("NAME")
password = os.getenv("PASSWORD")
mail = os.getenv("GMAIL")

BASE_URL = {
    "development": "https://practice-automation.com/",
    "staging": "https://practice-automation.com/",
    "production": "https://practice-automation.com/"
}
