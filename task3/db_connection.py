import psycopg2
import logging

# Configure basic logging
logging.basicConfig(level=logging.ERROR)

def get_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="library",
            user="postgres",
            password="Nabeel123",
            port=5432
        )

        # Create a cursor for table creation
        cur = conn.cursor()

        # Create books table first (parent table)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
              book_id SERIAL PRIMARY KEY,
              title VARCHAR(100),
              author VARCHAR(100),
              available BOOLEAN
        );
        """)

        conn.commit()
        cur.close()  # Close the cursor used for table creation

        # Create a new cursor for the caller
        cur = conn.cursor()
        return conn, cur

    except Exception as e:
        logging.error(f"Error connecting to database or creating table: {str(e)}")
        return None, None

