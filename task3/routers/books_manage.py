from db_connection import get_connection
from pydantic import BaseModel
from fastapi import APIRouter
import psycopg2
import logging


conn, curr = get_connection()


# ----------> defining the Schema <----------

class QueryRequest(BaseModel):
    book_id: int
    book_title: str
    book_author: str

class BorrowRequest(BaseModel):
    book_title: str


router = APIRouter(tags=["Books Management System"])



# ---------> Add the book <----------

@router.post("/add-books")
def add_books(request: QueryRequest):
    try:
        insert_query = """
            INSERT INTO books (book_id, title, author, available)
            VALUES (%s, %s, %s, %s)
        """
        curr.execute(insert_query, (
            request.book_id,
            request.book_title,
            request.book_author,
            True  # new book will be true
        ))
        
        conn.commit()
        return {"message": "Book successfully inserted and marked as available."}

    except Exception as e:
        logging.error(f"Error adding book: {str(e)}")
        return {"error": "Failed to add book."}



#  --------> Borrow the Book <---------

@router.put("/borrow-book")
def borrow_book(request: BorrowRequest):
    
    try:
        
        curr.execute("SELECT available FROM books where title=%s", (request.book_title,))
        
        result = curr.fetchone()
        
        if result is None:
            return {"message": f"No book in database with this {request.book_title}"}
        
        if not result[0]:
            return {"message": f"Book '{request.book_title}' is already borrowed."}
        
        
        #update book availablity
        
        update_query = """
            UPDATE books SET available=FALSE
            WHERE title=%s
        """
        
        curr.execute(update_query, (request.book_title,))
        
        conn.commit()
        return {"message": f"Book '{request.book_title}' successfully borrowed."}
    
    
    except Exception as e:
        logging.error(f"Error Borrowing book: {str(e)}")
        return {"error": "Failed to borrow book"}

        
        

#  ---------> Return the Book <--------

@router.put('/return-book')
def return_book(request: BorrowRequest):
    
    try:
        
        curr.execute("SELECT available FROM books where title=%s", (request.book_title,))
        
        result = curr.fetchone()
        
        if result is None:
            return {"message": f"No book in database with this {request.book_title}"}
        
        if result[0]:
            return {"message": f"Book '{request.book_title}' is already available"}
        

        update_query = "UPDATE books SET available=TRUE WHERE title=%s"
        curr.execute(update_query, (request.book_title,))
        conn.commit()
        
        

        return {"message": f"Book '{request.book_title}'  successfully returned."}
    
    
    except Exception as e:
        logging.error(f"Error returning book: {str(e)}")
        return {"error": "Failed to return book"}
    

# ----> Show all the books < ------

@router.get('/show-books')
def show_books():
    
    curr.execute("SELECT * FROM books where available=true")
    
    result = curr.fetchall()
    conn.commit()
    
    return {'message': result}