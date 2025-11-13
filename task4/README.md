<div align="center">

# 📚 Customer Order Management System

### A Modern Backend API for E-Commerce Operations

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)

[Features](#-features) • [Installation](#-installation) • [API Docs](#-api-endpoints) • [Tech Stack](#-tech-stack)

</div>

---

## 🎯 Overview

A high-performance backend API built with **FastAPI** for managing customers, books, and orders. This system provides complete CRUD operations with PostgreSQL database integration, following REST API best practices and modern Python standards.

## ✨ Features

<table>
  <tr>
    <td>⚡ <b>Blazing Fast</b></td>
    <td>Async request handling with FastAPI</td>
  </tr>
  <tr>
    <td>🗃️ <b>ORM Powered</b></td>
    <td>Type-safe operations with SQLAlchemy</td>
  </tr>
  <tr>
    <td>🐘 <b>PostgreSQL</b></td>
    <td>Robust relational database backend</td>
  </tr>
  <tr>
    <td>🧩 <b>Modular Design</b></td>
    <td>Clean architecture with separated routers</td>
  </tr>
  <tr>
    <td>📝 <b>Auto Validation</b></td>
    <td>Pydantic models for data integrity</td>
  </tr>
  <tr>
    <td>📚 <b>Interactive Docs</b></td>
    <td>Built-in Swagger UI and ReDoc</td>
  </tr>
</table>

## 🏗️ Project Structure

```
customer-order-management/
│
├── 📄 main.py                    # FastAPI application entry
├── 🔗 db_connection.py           # Database session manager
├── 📋 requirements.txt           # Python dependencies
│
├── 📁 models/                    # SQLAlchemy Models
│   ├── __init__.py
│   ├── customer.py               # Customer table schema
│   ├── book.py                   # Book table schema
│   └── order.py                  # Order table schema
│
├── 📁 schemas/                   # Pydantic Schemas
│   ├── __init__.py
│   ├── customer.py               # Customer validation models
│   ├── book.py                   # Book validation models
│   └── order.py                  # Order validation models
│
└── 📁 routers/                   # API Endpoints
    ├── __init__.py
    ├── customers.py              # /customers routes
    ├── books.py                  # /books routes
    └── orders.py                 # /orders routes
```

## 🚀 Installation

### Prerequisites

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12%2B-blue)

### Quick Start

**1️⃣ Clone Repository**
```bash
git clone https://github.com/nabeelbabar/customer-order-management.git
cd customer-order-management
```

**2️⃣ Setup Virtual Environment**
```bash
# Create environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

**3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Configure Database**

Update `db_connection.py` with your PostgreSQL credentials:
```python
DATABASE_URL = "postgresql://username:password@localhost:5432/order_management"
```

**5️⃣ Launch Server**
```bash
uvicorn main:app --reload
```

✅ Server running at: `http://localhost:8000`

## 📡 API Endpoints

### 👥 Customers

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/customers` | Retrieve all customers |
| `GET` | `/customers/{id}` | Get customer by ID |
| `POST` | `/customers` | Create new customer |
| `PUT` | `/customers/{id}` | Update customer details |
| `DELETE` | `/customers/{id}` | Delete customer |

### 📖 Books

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/books` | List all books |
| `GET` | `/books/{id}` | Get book by ID |
| `POST` | `/books` | Add new book |
| `PUT` | `/books/{id}` | Update book information |
| `DELETE` | `/books/{id}` | Remove book |

### 🛒 Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/orders` | Fetch all orders |
| `GET` | `/orders/{id}` | Get order by ID |
| `POST` | `/orders` | Place new order |
| `PUT` | `/orders/{id}` | Modify order |
| `DELETE` | `/orders/{id}` | Cancel order |

## 💡 Example Request

### Create New Customer

```bash
curl -X POST "http://localhost:8000/customers" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+92-300-1234567"
  }'
```

### Response

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "+92-300-1234567",
  "created_at": "2025-11-13T18:45:00"
}
```

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Modern async web framework |
| **SQLAlchemy** | Python SQL toolkit and ORM |
| **PostgreSQL** | Relational database system |
| **Pydantic** | Data validation library |
| **Uvicorn** | ASGI server implementation |

</div>

## 📚 API Documentation

Once the server is running, explore the interactive API documentation:

- **Swagger UI**: [`http://localhost:8000/docs`](http://localhost:8000/docs)
- **ReDoc**: [`http://localhost:8000/redoc`](http://localhost:8000/redoc)

## 🔧 Development

### Run Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black .
```

### Type Checking
```bash
mypy .
```

## 📦 Dependencies

Create `requirements.txt`:
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
pydantic==2.5.0
python-dotenv==1.0.0
```

## 🌟 Features Roadmap

- [ ] JWT Authentication
- [ ] Rate Limiting
- [ ] Redis Caching
- [ ] Docker Support
- [ ] CI/CD Pipeline
- [ ] Unit Tests Coverage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

<div align="center">

**Nabeel Babar**

AI & NLP Enthusiast | Full-Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nabeelbabar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/nabeelbabar)

</div>

---

<div align="center">

⭐ **If you find this project useful, please consider giving it a star!** ⭐

Made with ❤️ by Nabeel Babar

</div>
