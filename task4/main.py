from fastapi import FastAPI
import uvicorn

from routers.order_manage import router as order_router

app = FastAPI(
    title='Order Management System',
    description='This app will manage the orders of the users'
)


app.include_router(order_router, prefix='/ordermanage')

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=4545)