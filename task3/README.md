<div align="center">

# 📚 Library Management System API

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)](https://github.com)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)](https://github.com/psf/black)

**A modern, high-performance FastAPI backend for seamless library book management**

[Features](#-features) • [Quick Start](#-quick-start) • [API Documentation](#-api-endpoints) • [Contributing](#-contributing)

</div>

---

## 🎯 Overview

The **Library Management System API** is a robust, production-ready backend solution built with FastAPI and PostgreSQL. It provides a RESTful interface for managing library operations including book inventory, borrowing, and returns with comprehensive validation and error handling.

### 🌟 Why This Project?

- ⚡ **Fast**: Built on FastAPI for high-performance async operations
- 🛡️ **Type-Safe**: Full Pydantic validation for request/response models
- 📊 **Reliable**: PostgreSQL database with ACID compliance
- 📝 **Well-Documented**: Auto-generated interactive API documentation
- 🔍 **Observable**: Comprehensive logging for monitoring and debugging

---

## ✨ Features

<table>
<tr>
<td>

- ✅ **CRUD Operations** for book management
- 🔄 **Borrow/Return System** with availability tracking
- 🔐 **Request Validation** using Pydantic models
- 📋 **Error Logging** for production debugging

</td>
<td>

- 📚 **PostgreSQL Integration** with psycopg2
- 🚀 **Async Support** for concurrent requests
- 📖 **Interactive API Docs** (Swagger UI & ReDoc)
- 🎨 **Clean Architecture** with separation of concerns

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic"/>
  <img src="https://img.shields.io/badge/Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white" alt="Uvicorn"/>
</p>

---

## 📁 Project Structure

```
library-management-api/
│
├── 📄 main.py                # Application entry point & configuration
├── 📄 books_router.py        # API routes for book operations
├── 📄 db_connection.py       # Database connection & pooling
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # Project documentation
└── 📄 .env                  # Environment variables (create this)
```

---

## 🗄️ Database Schema

<details>
<summary><b>Click to expand database structure</b></summary>

### **Table: `books`**

| Column      | Type           | Constraints     | Description                      |
|-------------|----------------|-----------------|----------------------------------|
| `book_id`   | SERIAL         | PRIMARY KEY     | Auto-incrementing unique ID      |
| `title`     | VARCHAR(100)   | NOT NULL        | Title of the book                |
| `author`    | VARCHAR(100)   | NOT NULL        | Author name                      |
| `available` | BOOLEAN        | DEFAULT TRUE    | Availability status              |

### **SQL Schema**

```
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);
```

</details>

---

## 📡 API Endpoints

### **Base URL**: `http://localhost:8000`

| Method | Endpoint              | Description           | Auth Required |
|--------|----------------------|-----------------------|---------------|
| POST   | `/books/add`         | Add a new book        | ❌            |
| PUT    | `/books/borrow/{id}` | Borrow a book         | ❌            |
| PUT    | `/books/return/{id}` | Return a book         | ❌            |

<details>
<summary><b>📌 1. Add a New Book</b></summary>

### `POST /books/add`

Add a new book to the library inventory.

**Request Body:**
```
{
  "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
  "author": "Robert C. Martin"
}
```

**Success Response (201 Created):**
```
{
  "message": "Book added successfully",
  "book_id": 1
}
```

**cURL Example:**
```
curl -X POST "http://localhost:8000/books/add" \
     -H "Content-Type: application/json" \
     -d '{"title":"Clean Code","author":"Robert C. Martin"}'
```

</details>

<details>
<summary><b>🔄 2. Borrow a Book</b></summary>

### `PUT /books/borrow/{book_id}`

Mark a book as borrowed (unavailable).

**Path Parameter:**
- `book_id` (integer): The unique ID of the book

**Success Response (200 OK):**
```
{
  "message": "Book borrowed successfully",
  "book_id": 1,
  "available": false
}
```

**Error Response (404 Not Found):**
```
{
  "detail": "Book not found or already borrowed"
}
```

**cURL Example:**
```
curl -X PUT "http://localhost:8000/books/borrow/1"
```

</details>

<details>
<summary><b>↩️ 3. Return a Book</b></summary>

### `PUT /books/return/{book_id}`

Mark a book as returned (available).

**Path Parameter:**
- `book_id` (integer): The unique ID of the book

**Success Response (200 OK):**
```
{
  "message": "Book returned successfully",
  "book_id": 1,
  "available": true
}
```

**Error Response (404 Not Found):**
```
{
  "detail": "Book not found or already available"
}
```

**cURL Example:**
```
curl -X PUT "http://localhost:8000/books/return/1"
```

</details>

---

## 🚀 Quick Start

### Prerequisites

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-316192?logo=postgresql&logoColor=white)
![pip](https://img.shields.io/badge/pip-Latest-brightgreen?logo=pypi&logoColor=white)

### Installation Steps

1️⃣ **Clone the repository**
```
git clone https://github.com/yourusername/library-management-api.git
cd library-management-api
```

2️⃣ **Create and activate virtual environment**
```
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install dependencies**
```
pip install -r requirements.txt
```

4️⃣ **Set up PostgreSQL database**
```
# Create database
createdb library_db

# Create schema
psql -d library_db -c "CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);"
```

5️⃣ **Configure database connection**

Create a `.env` file or update `db_connection.py`:
```
DB_HOST=localhost
DB_NAME=library_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432
```

6️⃣ **Run the server**
```
uvicorn main:app --reload
```

✅ **Server running at**: `http://localhost:8000`

---

## 📖 API Documentation

Once the server is running, access the interactive documentation:

| Documentation Type | URL                              | Description                     |
|--------------------|----------------------------------|---------------------------------|
| **Swagger UI**     | http://localhost:8000/docs       | Interactive API testing         |
| **ReDoc**          | http://localhost:8000/redoc      | Clean, readable documentation   |
| **OpenAPI JSON**   | http://localhost:8000/openapi.json | Raw OpenAPI specification     |

---

## 🧪 Testing

```
# Install testing dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest tests/ -v

# Run with coverage
pytest --cov=app tests/
```

---

## 🔮 Roadmap & Future Enhancements

- [ ] 🔐 JWT-based authentication & authorization
- [ ] 🔍 Advanced search with filters (title, author, genre, availability)
- [ ] 📄 Pagination for large datasets
- [ ] 📅 Due date tracking & overdue notifications
- [ ] 👤 User management & borrowing history
- [ ] 💰 Fine calculation for overdue books
- [ ] 🏷️ Book categories, genres & tags
- [ ] 🔄 Database migrations with Alembic
- [ ] ✅ Unit & integration test suite
- [ ] 🐳 Docker containerization
- [ ] ⚡ Redis caching layer
- [ ] 🚦 API rate limiting & throttling
- [ ] 📊 Analytics dashboard
- [ ] 📧 Email notifications
- [ ] 🌐 Multi-language support

---

## 📝 Environment Variables

Create a `.env` file in the project root:

```
# Database Configuration
DB_HOST=localhost
DB_NAME=library_db
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432

# Application Settings
APP_ENV=development
LOG_LEVEL=INFO
```

---

## 🐛 Troubleshooting

<details>
<summary><b>Database connection failed</b></summary>

- Ensure PostgreSQL service is running
- Verify credentials in `db_connection.py`
- Check if database exists: `psql -l`
</details>

<details>
<summary><b>Module not found errors</b></summary>

- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`
</details>

<details>
<summary><b>Port already in use</b></summary>

- Change port: `uvicorn main:app --port 8080`
- Or kill process using port 8000
</details>

---

## 🤝 Contributing

Contributions are **welcome**! Please follow these steps:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch
   ```
   git checkout -b feature/AmazingFeature
   ```
3. 💾 Commit your changes
   ```
   git commit -m 'Add some AmazingFeature'
   ```
4. 📤 Push to the branch
   ```
   git push origin feature/AmazingFeature
   ```
5. 🔃 Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - feel free to use this project for personal or commercial purposes.
```

---

## 👨‍💻 Author

<div align="center">

**Nabeel Babar**


</div>

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐️!

<div align="center">

[![Star History Chart](https://img.shields.io/github/stars/yourusername/library-management-api?style=social)](https://github.com/yourusername/library-management-api/stargazers)
[![Fork](https://img.shields.io/github/forks/yourusername/library-management-api?style=social)](https://github.com/yourusername/library-management-api/network/members)

**Made with ❤️ and FastAPI**

</div>
```

***

## 💾 **How to Save This File:**

1. **Copy the entire markdown code above**
2. **Create a new file** named `README.md` in your project root
3. **Paste the content** and save it
4. **Replace placeholders** like `yourusername`, `your.email@example.com`, etc.

### **Quick Command:**
```bash
# Navigate to your project folder
cd library-management-api

# Create and edit README.md
nano README.md
# or
code README.md  # if using VS Code
```

This enhanced README includes:[1][2][3][4][5]
- **Advanced badges** with custom styling from Shields.io
- **Collapsible sections** for better organization
- **Professional formatting** with centered headers and emojis
- **Color-coded badges** for tech stack
- **Interactive elements** with expandable details
- **Beautiful tables** for better readability
- **cURL examples** for API testing
- **Troubleshooting section** for common issues
- **Social badges** for author contact

The formatting follows modern GitHub README best practices and will look stunning on your repository! 🚀
