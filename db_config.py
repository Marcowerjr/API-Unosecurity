from flask_pymongo import pymongo 
import os 


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.en1r6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.users



