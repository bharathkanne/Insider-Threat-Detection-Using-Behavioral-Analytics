import time
import json
import mysql.connector
from mysql.connector import Error

LOG_FILE_PATH = r'C:\Users\bhara.KBHARATH\Downloads\onepro\insider-threat-env\app.log'  # Path to your log file

def create_connection():
    """Create a database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='bharathrdj',  # Replace with your password
            database='myy1'  # Replace with your database name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def log_to_mysql(log_message):
    """Insert log message into the database."""
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO activity_logs (log_type, log_message) 
    VALUES (%s, %s);
    """
    values = ('Info', log_message)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Log message saved to MySQL")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        cursor.close()
        connection.close()

def tail_log_file():
    """Tail the log file and monitor new entries."""
    with open(LOG_FILE_PATH, 'r') as file:
        # Move to the end of the file
        file.seek(0, 2)
        
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly to avoid busy waiting
                continue
            
            # Here you can parse the log line as needed
            log_message = line.strip()  # Remove any extra whitespace
            log_to_mysql(log_message)  # Save log message to MySQL

if __name__ == "__main__":
    tail_log_file()
