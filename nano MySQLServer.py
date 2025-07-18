import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # replace with your MySQL username
            password="12345678"  # replace with your MySQL password
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print("Error while connecting to MySQL:", e)
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

create_database()
