from pymongo import MongoClient
from env import ENV_VARS

mongo_client = MongoClient(ENV_VARS.DB_CONNECTION_STRING)
db = mongo_client[ENV_VARS.DB_NAME]

QUESTIONS = db["questions"]
