#Parrish Ward // 6-19-21 // Module 5.2 - mongodb_test.py // Test program for connecting to a  MongoDB Atlas cluster

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

client = MongoClient(url)
db = client.pytech

print("\n Pytech collection list")
print(db.list_collection_names())
