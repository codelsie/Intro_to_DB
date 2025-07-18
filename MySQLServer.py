import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='codelsie',
            password='12345678'  # replace with your real password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                # Optional: print("MySQL connection is closed")
        except:
            pass

# Run the function
create_database()
