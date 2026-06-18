from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

connect(host=os.getenv("MONGO_URL"))

