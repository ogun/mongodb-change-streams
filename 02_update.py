from pymongo import MongoClient

client = MongoClient("mongodb://root:password123@localhost/test?authSource=admin")
db = client.get_default_database()

db.users.update_one({"username": "ogun"}, {"$set": {"age": 37}})
