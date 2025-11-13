from fastapi import FastAPI
from routers.books_manage import router as books_router
import uvicorn

app = FastAPI(
    title="Library Management System",
    description="A FastAPI-based backend for managing books in the library database using PostgreSQL.",
    version="1.0.0"
)

app.include_router(books_router, prefix='/bookapi')

if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=4545)