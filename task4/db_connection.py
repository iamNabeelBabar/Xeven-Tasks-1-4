import psycopg2
import logging

logging.basicConfig(level=logging.ERROR)

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="orders",
            user="postgres",
            password="Nabeel123",
            port=5432
        )


        curr = conn.cursor()
        
        return conn, curr
    
    except Exception as e:
        logging.error(f"Error connecting to database or creating table: {str(e)}")
        return None, None

