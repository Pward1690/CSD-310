#Parrish Ward // 7-2-21 // Module 5.2 - mongodb_test.py // Test program for connecting to a  MongoDB Atlas cluster

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

client = MongoClient(url)
db = client.pytech

students = db.collection

fred = {
    "student_id":"1007",
    "first_name":"Fred",
    "last_name":"Hammond",
}
 
fred_student_id = students.insert_one(fred).inserted_id

print(fred_student_id)

steve = {
    "student_id": "1008",
    "first_name": "Steve",
    "last_name": "Micheals",
}
 
steve_student_id = students.insert_one(steve).inserted_id

print(steve_student_id)

hank = {
    "student_id": "1009",
    "first_name": "Hank",
    "last_name": "Aaron"
}
 
hank_student_id = students.insert_one(hank).inserted_id

print(hank_student_id)



print(db.list_collection_names())