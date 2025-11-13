<div align="center">

# 📂 Xeven Tasks 1–4

### Comprehensive Python Programming Exercises Collection

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A curated collection of Python programming exercises covering text processing, HR automation, and modern web API development.

[Overview](#-overview) • [Installation](#-installation) • [Tasks](#-tasks-at-a-glance) • [Usage](#-usage)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Tasks at a Glance](#-tasks-at-a-glance)
- [Installation](#-installation)
- [Usage](#-usage)
- [Task Details](#-task-details)
  - [Task 1: File Analyzer](#task-1-file-analyzer)
  - [Task 2: Employee Salary Adjustment](#task-2-employee-salary-adjustment)
  - [Task 3: Library Management System](#task-3-library-management-system)
  - [Task 4: Order Management System](#task-4-order-management-system)
- [Project Structure](#-project-structure)
- [Repository Topics](#-repository-topics)
- [License](#-license)
- [Author](#-author)
- [Contributing Notes](#-contributing-notes)

---

## 🎯 Overview

This repository contains four independent Python programming exercises designed to demonstrate proficiency in:
- Text processing and file manipulation
- Data analysis and transformation
- RESTful API development with FastAPI
- Database design and PostgreSQL integration
- Clean code practices and modular architecture

Each task is self-contained within its own subdirectory with dedicated Python scripts and supporting files.

---

## 📊 Tasks at a Glance

| Task | Title | Category | Technology Stack | Status |
|------|-------|----------|------------------|--------|
| **Task 1** | File Analyzer | Text Processing | Python, File I/O | ✅ Complete |
| **Task 2** | Employee Salary Adjustment | HR & Finance | Python, CSV Processing | ✅ Complete |
| **Task 3** | Library Management System | Web API | FastAPI, PostgreSQL, SQLAlchemy | ✅ Complete |
| **Task 4** | Order Management System | Web API | FastAPI, PostgreSQL, SQLAlchemy | ✅ Complete |

---

## 🚀 Installation

### Prerequisites

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12%2B-blue)

### Quick Setup

**1️⃣ Clone the Repository**
```bash
git clone https://github.com/nabeelbabar/xeven-tasks.git
cd xeven-tasks
```

**2️⃣ Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

**3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Setup PostgreSQL Database**
```bash
# Create databases for Task 3 and Task 4
createdb library_management
createdb order_management
```

---

## 💻 Usage

### Python Scripts (Tasks 1-2)
Navigate to the specific task directory and run the Python script:

```bash
# Task 1
cd task1
python file_analyzer.py

# Task 2
cd task2
python salary_adjustment.py
```

### FastAPI Applications (Tasks 3-4)
Navigate to the task directory and start the Uvicorn server:

```bash
# Task 3
cd task3
uvicorn main:app --reload --port 8001

# Task 4
cd task4
uvicorn main:app --reload --port 8002
```

---

## 📖 Task Details

### Task 1: File Analyzer

**📁 Directory:** `task1/`

#### Description
A robust text file analysis tool that processes input files and generates comprehensive statistics including word count, character count, line count, and frequency analysis.

#### Features
- ✅ Word and character counting
- ✅ Line-by-line analysis
- ✅ Word frequency distribution
- ✅ Case-insensitive processing
- ✅ Special character handling
- ✅ Formatted output report

#### Usage

```bash
cd task1
python file_analyzer.py
```

#### Input Example

`input.txt`:
```text
Hello World! This is a test file.
Python programming is amazing.
Hello Python!
```

#### Output Example

```text
=== FILE ANALYSIS REPORT ===

Total Lines: 3
Total Words: 12
Total Characters: 78

--- Word Frequency ---
hello: 2
python: 2
is: 2
world: 1
this: 1
a: 1
test: 1
file: 1
programming: 1
amazing: 1

=== END OF REPORT ===
```

#### Files
- `file_analyzer.py` - Main analysis script
- `input.txt` - Sample input file
- `output.txt` - Generated analysis report

---

### Task 2: Employee Salary Adjustment

**📁 Directory:** `task2/`

#### Description
An HR automation tool that processes employee records and applies salary adjustments based on predefined business rules. Supports bulk processing and generates formatted reports for payroll systems.

#### Features
- ✅ CSV/JSON data parsing
- ✅ Conditional salary adjustment logic
- ✅ Performance-based calculations
- ✅ Department-wise processing
- ✅ Automated report generation
- ✅ Data validation and error handling

#### Usage

```bash
cd task2
python salary_adjustment.py
```

#### Input Example

`employees.csv`:
```csv
employee_id,name,department,current_salary,performance_rating
101,John Doe,Engineering,50000,4.5
102,Jane Smith,Marketing,45000,3.8
103,Bob Johnson,Engineering,55000,4.2
```

#### Processing Rules
- **Performance Rating ≥ 4.0:** 10% salary increase
- **Performance Rating 3.5–3.9:** 5% salary increase
- **Performance Rating < 3.5:** No adjustment

#### Output Example

`adjusted_salaries.csv`:
```csv
employee_id,name,department,previous_salary,new_salary,adjustment_percentage
101,John Doe,Engineering,50000,55000,10%
102,Jane Smith,Marketing,45000,47250,5%
103,Bob Johnson,Engineering,55000,60500,10%
```

#### Files
- `salary_adjustment.py` - Main processing script
- `employees.csv` - Input employee data
- `adjusted_salaries.csv` - Output report

---

### Task 3: Library Management System

**📁 Directory:** `task3/`

#### Description
A comprehensive RESTful API for managing library operations including books, members, and borrowing transactions. Built with FastAPI for high-performance async operations and PostgreSQL for reliable data persistence.

#### Features
- ✅ **Book Management** - Add, update, delete, and search books
- ✅ **Member Management** - Register and manage library members
- ✅ **Borrowing System** - Track book loans and returns
- ✅ **FastAPI Routers** - Modular endpoint organization
- ✅ **SQLAlchemy ORM** - Type-safe database operations
- ✅ **Pydantic Validation** - Automatic request/response validation
- ✅ **PostgreSQL Database** - Robust relational data storage
- ✅ **Auto Documentation** - Interactive Swagger UI and ReDoc

#### Technology Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Server:** Uvicorn

#### Installation & Setup

```bash
cd task3

# Configure database connection in db_connection.py
DATABASE_URL = "postgresql://user:password@localhost:5432/library_management"

# Run the application
uvicorn main:app --reload --port 8001
```

#### API Endpoints

**📚 Books**
```bash
GET    /books              # List all books
GET    /books/{id}         # Get book details
POST   /books              # Add new book
PUT    /books/{id}         # Update book
DELETE /books/{id}         # Delete book
GET    /books/search?q=... # Search books
```

**👥 Members**
```bash
GET    /members            # List all members
GET    /members/{id}       # Get member details
POST   /members            # Register new member
PUT    /members/{id}       # Update member info
DELETE /members/{id}       # Remove member
```

**📖 Borrowing**
```bash
GET    /borrowings         # List all transactions
POST   /borrowings         # Borrow a book
PUT    /borrowings/{id}    # Return a book
GET    /borrowings/overdue # Get overdue books
```

#### Example Request

**Add New Book:**
```bash
curl -X POST "http://localhost:8001/books" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "isbn": "978-0132350884",
    "published_year": 2008,
    "quantity": 5
  }'
```

**Response:**
```json
{
  "id": 1,
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "978-0132350884",
  "published_year": 2008,
  "quantity": 5,
  "available": 5,
  "created_at": "2025-11-13T18:53:00"
}
```

#### API Documentation
- **Swagger UI:** `http://localhost:8001/docs`
- **ReDoc:** `http://localhost:8001/redoc`

#### Files
- `main.py` - FastAPI application entry point
- `db_connection.py` - Database configuration
- `models/` - SQLAlchemy database models
- `schemas/` - Pydantic validation schemas
- `routers/` - Modular API endpoints
  - `books.py` - Book management routes
  - `members.py` - Member management routes
  - `borrowings.py` - Borrowing system routes

---

### Task 4: Order Management System

**📁 Directory:** `task4/`

#### Description
A production-ready order management API for e-commerce operations. Handles customer orders, product inventory, and order processing workflows with PostgreSQL backend for transactional integrity.

#### Features
- ✅ **Customer Management** - CRUD operations for customers
- ✅ **Product Catalog** - Inventory and product management
- ✅ **Order Processing** - Create and track customer orders
- ✅ **Order Items** - Detailed line-item management
- ✅ **Status Tracking** - Order lifecycle management
- ✅ **FastAPI Framework** - Modern async API development
- ✅ **PostgreSQL Database** - ACID-compliant transactions
- ✅ **SQLAlchemy ORM** - Elegant database interactions
- ✅ **RESTful Design** - Standard HTTP methods

#### Technology Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Server:** Uvicorn

#### Installation & Setup

```bash
cd task4

# Configure database connection in db_connection.py
DATABASE_URL = "postgresql://user:password@localhost:5432/order_management"

# Run the application
uvicorn main:app --reload --port 8002
```

#### API Endpoints

**👤 Customers**
```bash
GET    /customers          # List all customers
GET    /customers/{id}     # Get customer details
POST   /customers          # Create new customer
PUT    /customers/{id}     # Update customer
DELETE /customers/{id}     # Delete customer
```

**📦 Products**
```bash
GET    /products           # List all products
GET    /products/{id}      # Get product details
POST   /products           # Add new product
PUT    /products/{id}      # Update product
DELETE /products/{id}      # Delete product
GET    /products/low-stock # Get low inventory items
```

**🛒 Orders**
```bash
GET    /orders             # List all orders
GET    /orders/{id}        # Get order details
POST   /orders             # Create new order
PUT    /orders/{id}        # Update order status
DELETE /orders/{id}        # Cancel order
GET    /orders/customer/{customer_id}  # Get customer orders
```

**📋 Order Items**
```bash
GET    /orders/{order_id}/items        # List order items
POST   /orders/{order_id}/items        # Add item to order
DELETE /orders/{order_id}/items/{id}   # Remove order item
```

#### Example Request

**Create New Order:**
```bash
curl -X POST "http://localhost:8002/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "items": [
      {
        "product_id": 5,
        "quantity": 2,
        "unit_price": 29.99
      },
      {
        "product_id": 8,
        "quantity": 1,
        "unit_price": 149.99
      }
    ],
    "status": "pending"
  }'
```

**Response:**
```json
{
  "id": 101,
  "customer_id": 1,
  "order_date": "2025-11-13T18:53:00",
  "status": "pending",
  "total_amount": 209.97,
  "items": [
    {
      "id": 1,
      "product_id": 5,
      "quantity": 2,
      "unit_price": 29.99,
      "subtotal": 59.98
    },
    {
      "id": 2,
      "product_id": 8,
      "quantity": 1,
      "unit_price": 149.99,
      "subtotal": 149.99
    }
  ]
}
```

#### Order Status Flow
```
pending → confirmed → processing → shipped → delivered → completed
                                         ↓
                                    cancelled
```

#### API Documentation
- **Swagger UI:** `http://localhost:8002/docs`
- **ReDoc:** `http://localhost:8002/redoc`

#### Files
- `main.py` - FastAPI application entry point
- `db_connection.py` - Database configuration
- `models/` - SQLAlchemy database models
- `schemas/` - Pydantic validation schemas
- `routers/` - Modular API endpoints
  - `customers.py` - Customer management routes
  - `products.py` - Product catalog routes
  - `orders.py` - Order processing routes
  - `order_items.py` - Order line items routes

---

## 📂 Project Structure

```
xeven-tasks/
│
├── 📄 README.md                      # This file
├── 📄 LICENSE                        # MIT License
├── 📄 requirements.txt               # Python dependencies
│
├── 📁 task1/                         # File Analyzer
│   ├── file_analyzer.py              # Main script
│   ├── input.txt                     # Sample input
│   ├── output.txt                    # Generated output
│   └── README.md                     # Task-specific docs
│
├── 📁 task2/                         # Employee Salary Adjustment
│   ├── salary_adjustment.py          # Main script
│   ├── employees.csv                 # Input data
│   ├── adjusted_salaries.csv         # Output report
│   └── README.md                     # Task-specific docs
│
├── 📁 task3/                         # Library Management System
│   ├── main.py                       # FastAPI entry point
│   ├── db_connection.py              # Database config
│   ├── models/                       # SQLAlchemy models
│   │   ├── book.py
│   │   ├── member.py
│   │   └── borrowing.py
│   ├── schemas/                      # Pydantic schemas
│   │   ├── book.py
│   │   ├── member.py
│   │   └── borrowing.py
│   ├── routers/                      # API endpoints
│   │   ├── books.py
│   │   ├── members.py
│   │   └── borrowings.py
│   └── README.md                     # Task-specific docs
│
└── 📁 task4/                         # Order Management System
    ├── main.py                       # FastAPI entry point
    ├── db_connection.py              # Database config
    ├── models/                       # SQLAlchemy models
    │   ├── customer.py
    │   ├── product.py
    │   ├── order.py
    │   └── order_item.py
    ├── schemas/                      # Pydantic schemas
    │   ├── customer.py
    │   ├── product.py
    │   ├── order.py
    │   └── order_item.py
    ├── routers/                      # API endpoints
    │   ├── customers.py
    │   ├── products.py
    │   ├── orders.py
    │   └── order_items.py
    └── README.md                     # Task-specific docs
```

---

## 🏷️ Repository Topics

Consider adding these topics to your GitHub repository for better discoverability:

```
python
fastapi
postgresql
sqlalchemy
rest-api
api-development
text-processing
automation
hr-automation
library-management
order-management
e-commerce
backend
python3
async
uvicorn
pydantic
orm
database
crud
```

**How to add topics on GitHub:**
1. Navigate to your repository
2. Click "About" (gear icon) in the top-right
3. Add topics in the "Topics" field
4. Save changes

---

## 📦 Dependencies

Create `requirements.txt`:
```txt
# Core Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0

# Database
sqlalchemy==2.0.23
psycopg2-binary==2.9.9

# Validation
pydantic==2.5.0

# Utilities
python-dotenv==1.0.0
python-multipart==0.0.6
```

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Nabeel Babar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Author

<div align="center">

**Nabeel Babar**

BS AI Student | NLP Enthusiast | Full-Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nabeelbabar)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/nabeelbabar)

</div>

---

## 📝 Contributing Notes

### For Contributors

If you're contributing to this repository, please ensure:

1. **Code Quality Standards:**
   - Follow PEP 8 style guidelines
   - Add docstrings for functions and classes
   - Include type hints where applicable
   - Write meaningful commit messages

2. **API Development:**
   - Use async/await patterns for FastAPI routes
   - Implement proper error handling
   - Add request/response examples
   - Document all endpoints

3. **Database Management:**
   - Use SQLAlchemy migrations (Alembic)
   - Follow normalization principles
   - Add database indexes for performance
   - Implement proper foreign key relationships

4. **Testing:**
   - Write unit tests for business logic
   - Add integration tests for API endpoints
   - Test edge cases and error scenarios
   - Maintain test coverage above 80%

5. **Documentation:**
   - Update task-specific README files
   - Include API usage examples
   - Document environment variables
   - Add setup instructions

### Development Checklist
- [ ] Code follows PEP 8 standards
- [ ] All tests passing
- [ ] API endpoints documented
- [ ] Database schema documented
- [ ] README updated
- [ ] Dependencies listed in requirements.txt

---

<div align="center">

⭐ **Star this repository if you find it helpful!** ⭐

Made with 💙 by Nabeel Babar | 2025

</div>
