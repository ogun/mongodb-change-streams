from pymongo import MongoClient

client = MongoClient("mongodb://root:password123@localhost/test?authSource=admin")
db = client.get_default_database()

db.users.replace_one({"username": "ogun"}, {"username": "ogun", "age": 38})
