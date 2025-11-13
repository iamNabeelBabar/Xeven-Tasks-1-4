from db_connection import get_connection


def books_insertion():
    conn = None
    cur = None

    try:
        conn, cur = get_connection()

        sql_query = "INSERT INTO books (book_id, title, author, available) VALUES (%s, %s, %s, %s)"
        
        data_to_insert =[
            (1, 'psycology of money', 'Morgan Housal', '1'),
            (2, 'eat that frog', 'Ahmed', '0'),
            (3, 'power to say no', 'darth mout', '1'),
            (4, 'nothing will happen wrong', 'Einstein', '1'),
            (5, 'the way of glory', 'Javed Iqbal', '1'),
            
        ] 


        cur.executemany(sql_query, data_to_insert)

        conn.commit()
        print('Data inserted successfully')

    except Exception as e:
        print('error inserting data', e)
        if conn:
            conn.rollback()
            
    finally:
        if cur:
            cur.close()
            
        if conn:
            conn.close()




def show_books():
    conn = None
    cur = None

    try:
        conn, cur = get_connection()

        sql_query = "SELECT * FROM books"
        cur.execute(sql_query)
        books = cur.fetchall()   

        print("All Books in Library:\n")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available: {book[3]}")

    except Exception as e:
        print('Error fetching data:', e)
        if conn:
            conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

show_books()