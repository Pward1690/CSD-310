#Alpha Group
#Parrish Ward, Aurora Lopez, Lucas Ramsey, Rusty Degarmo, Mitchell Kwon
#Module 11 - 7.15.21 - Milestone 3 (Equipment Age Counter)

import mysql.connector

#connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "Tayeandmissy08",
    database= "outlandadventures"
)

#create a cursor
cursor = db.cursor()

#Count how much equipment older than five years old
cursor.execute('SELECT COUNT(*) FROM supplies WHERE CAST(date_added AS DATE) < NOW() - interval 5 year;')

info = cursor.fetchall()


print()
print("-- DISPLAYING SUPPLIES RECORDS --")
print(f"Equipment older than 5 years: {info[0][0]}")
print()

#close the database
db.close()