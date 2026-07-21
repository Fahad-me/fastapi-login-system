# 🔐 FastAPI Login System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116.1-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**A modern authentication system built with FastAPI, PostgreSQL, SQLAlchemy, JWT, and Jinja2 Templates.**

</div>

---

## 📖 Overview

This project is a **complete authentication system** developed using **FastAPI** and **PostgreSQL**.

It demonstrates industry-standard backend development practices including:

- User Registration
- Secure Login
- Password Hashing using bcrypt
- JWT Authentication
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Environment Variables
- REST API Documentation (Swagger UI)
- HTML Templates with Jinja2

This project is ideal for learning FastAPI authentication and serves as a strong backend portfolio project.

---

# 🚀 Features

- ✅ User Registration
- ✅ User Login
- ✅ JWT Token Generation
- ✅ Password Hashing (bcrypt)
- ✅ PostgreSQL Database
- ✅ SQLAlchemy ORM
- ✅ Pydantic Validation
- ✅ Environment Variables (.env)
- ✅ Swagger API Documentation
- ✅ Modular Project Structure
- ✅ Static Files Support
- ✅ HTML Templates

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python 3.13 | Programming Language |
| FastAPI | Backend Framework |
| PostgreSQL 17 | Database |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| Jinja2 | HTML Templates |
| JWT | Authentication |
| bcrypt | Password Hashing |
| Uvicorn | ASGI Server |

---

# 📂 Project Structure

```text
fastapi-login-system/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   └── users.py
│   │
│   ├── schemas/
│   │   └── user.py
│   │
│   ├── services/
│   │   └── auth_service.py
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   │
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🗄 Database Schema

### users

| Column | Type |
|---------|------|
| id | Integer |
| full_name | VARCHAR(100) |
| username | VARCHAR(50) |
| email | VARCHAR(100) |
| password | VARCHAR(255) |
| is_active | Boolean |
| created_at | Timestamp |
| updated_at | Timestamp |

---

# 📡 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and generate JWT |

---

## Users

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/users/profile` | User Profile |
| GET | `/users/dashboard` | User Dashboard |

---

## General

| Method | Endpoint |
|---------|----------|
| GET | `/` |
| GET | `/health` |

---

# 📷 Screenshots

## Swagger Documentation

> docs/swagger.png

```
docs/swagger.png
```

---

## PostgreSQL Database

> docs/database.png

```
docs/database.png
```

---

## Login Page

> docs/login.png

```
docs/login.png
```

---

## Dashboard

> docs/dashboard.png

```
docs/dashboard.png
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/Fahad-me/fastapi-login-system.git

cd fastapi-login-system
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create

```
.env
```

Example

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/fastapi_login_db

SECRET_KEY=YOUR_SECRET_KEY

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run Server

```bash
uvicorn app.main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# 🔒 Authentication Flow

```
User

↓

Register

↓

Password Hashing (bcrypt)

↓

PostgreSQL

↓

Login

↓

Verify Password

↓

Generate JWT

↓

Authenticated User
```

---

# 🔐 Security Features

- Password Hashing
- JWT Authentication
- Email Validation
- SQLAlchemy ORM
- Environment Variables
- Input Validation
- Secure Password Storage

---

# 📌 Future Improvements

- User Logout
- Refresh Tokens
- Email Verification
- Password Reset
- OAuth Login (Google/GitHub)
- Role-Based Authentication
- Docker Support
- Alembic Database Migrations
- Unit Testing
- CI/CD Pipeline
- Redis Session Management

---

# 👨‍💻 Author

**Fahad Abdullah**

🎓 B.Tech – Artificial Intelligence & Machine Learning

📍 Greater Noida, India

GitHub

<https://github.com/Fahad-me>

LinkedIn

(Add your LinkedIn profile)

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future development.

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

Made with ❤️ using FastAPI & PostgreSQL


we also made 
 ├── Development_Journal.md
│   ├── Project_Report.md
│   ├── Interview_Notes.md
│   ├── Bugs_and_Solutions.md
│   ├── Git_History.md
│   ├── API_Documentation.md
│   ├── Deployment_Guide.md
│   └── Future_Roadmap.md

</div>
