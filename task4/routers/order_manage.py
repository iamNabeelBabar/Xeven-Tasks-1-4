from fastapi import APIRouter
from db_connection import get_connection
from pydantic import BaseModel
import psycopg2


conn, curr = get_connection()


router = APIRouter(tags=["Order Management System"])


@router.get("/show-orders")
def show_order():
    
    
    curr.execute("""SELECT 
            o.order_id,
            c.name AS customer_name,
            c.email AS customer_email,
            o.product_name,
            o.amount
        FROM orders o                                            #---------------------> i use Chatgpt For this query (applogies for that)
        JOIN customers c ON o.customer_id = c.customer_id
        ORDER BY o.order_id;
        """)
    
    
    result = curr.fetchall()
        
    orders = [
            {
                "order_id": row[0],
                "customer_name": row[1],
                "customer_email": row[2],
                "product_name": row[3],
                "amount": float(row[4]) 
            } for row in result
        ]
        
    return {"orders": orders}



class OrderRequest(BaseModel):
    order_id: int
    new_amount: float
    


@router.put("/update-order/{order_id}/{new_amount}")

def update_order_amount(request: OrderRequest):
    try:
        update_query = """
            UPDATE orders
            SET amount = %s
            WHERE order_id = %s
        """
        
        curr.execute(update_query, (request.new_amount, request.order_id))
        conn.commit()
        
        return {"message": "Order amount updated successfully."}
    
    except Exception as e:
        return {"error": f"Failed to update order amount: {str(e)}"}