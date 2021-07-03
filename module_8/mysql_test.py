"Parrish Ward / 7-3-21 / Module 8."



import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "pysports_user",
    "password": "Tayeandmissy08",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
     

    db = mysql.connector.connect(**config)  
    
    
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database does not exist")

    else:
        print(err)

finally:
    

    db.close()
