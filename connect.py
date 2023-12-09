import mysql.connector

try:

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    if db.is_connected():
        print("Connected to MySQL")

except mysql.connector.Error as error:
    print(f"Failed to connect: {error}")

finally:
    if db.is_connected():
        db.close()
        print("MySQL connection is closed")