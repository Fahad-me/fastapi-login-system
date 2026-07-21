# 🌐 FastAPI Authentication Platform

# API Documentation

---

# Document Information

**Project**

FastAPI Authentication Platform

**Version**

1.0

**Developer**

Fahad Abdullah

**Framework**

FastAPI

---

# About

This document explains every API endpoint used in the project.

Each API contains:

- Purpose
- URL
- HTTP Method
- Request Body
- Response
- Files Involved
- Authentication
- Future Improvements

---

# Base URL

Development

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# API Architecture

```
Browser

↓

FastAPI Route

↓

Service Layer

↓

SQLAlchemy ORM

↓

PostgreSQL

↓

Response

↓

Browser
```

---

# Authentication APIs

---

# 1. Register Page

## Endpoint

```
GET /auth/register
```

### Purpose

Displays the HTML registration page.

### Request Body

None

### Response

```
register.html
```

### Authentication

No

### Files

```
app/routes/auth.py

app/templates/register.html
```

---

# 2. HTML Register

## Endpoint

```
POST /auth/register-form
```

### Purpose

Receives HTML form data and creates a new user.

### Request

```
full_name

username

email

password
```

### Process

```
HTML Form

↓

Form()

↓

UserCreate

↓

register_user()

↓

PostgreSQL

↓

Redirect Login
```

### Success Response

```
303 Redirect

/auth/login
```

### Authentication

No

### Files

```
auth.py

auth_service.py

user.py

database.py
```

---

# 3. Register API

## Endpoint

```
POST /auth/register
```

### Purpose

Registration endpoint for Swagger API.

### Request Body

JSON

```json
{
    "full_name":"Fahad Abdullah",
    "username":"fahad",
    "email":"abc@gmail.com",
    "password":"123456"
}
```

### Success Response

```json
{
    "id":1,
    "full_name":"Fahad Abdullah",
    "username":"fahad",
    "email":"abc@gmail.com"
}
```

### Authentication

No

---

# 4. Login Page

## Endpoint

```
GET /auth/login
```

### Purpose

Displays Login page.

### Authentication

No

### Response

```
login.html
```

---

# 5. HTML Login

## Endpoint

```
POST /auth/login-form
```

### Purpose

Authenticate HTML user.

### Request

```
email

password
```

### Process

```
HTML Form

↓

authenticate_user()

↓

Verify Password

↓

Generate JWT

↓

Set Cookie

↓

Redirect Dashboard
```

### Success Response

```
303 Redirect

/users/dashboard
```

### Cookie

```
access_token
```

### Authentication

No

---

# 6. Login API

## Endpoint

```
POST /auth/login
```

### Purpose

Swagger Login API.

### Request

```json
{
    "email":"abc@gmail.com",
    "password":"123456"
}
```

### Success Response

```json
{
    "access_token":"JWT_TOKEN",
    "token_type":"bearer"
}
```

### Authentication

No

---

# User APIs

---

# 7. Dashboard

## Endpoint

```
GET /users/dashboard
```

### Purpose

Displays dashboard after login.

### Authentication

Yes

### Process

```
Cookie

↓

JWT

↓

Decode Token

↓

Get User

↓

Dashboard
```

### Response

```
dashboard.html
```

### Files

```
users.py

dashboard.html
```

---

# 8. Profile

## Endpoint

```
GET /users/profile
```

### Purpose

Displays user profile.

### Status

🚧 Planned

### Authentication

Yes

---

# System APIs

---

# 9. Home

## Endpoint

```
GET /
```

### Purpose

Displays landing page.

### Authentication

No

### Response

```
home.html
```

---

# 10. Health Check

## Endpoint

```
GET /health
```

### Purpose

Verify application status.

### Response

```json
{
    "status":"OK",
    "application":"FastAPI Authentication System"
}
```

---

# Authentication Flow

```
User

↓

Login Page

↓

FastAPI

↓

Database

↓

Verify Password

↓

Generate JWT

↓

Cookie

↓

Dashboard
```

---

# Registration Flow

```
Register Form

↓

FastAPI

↓

Validation

↓

bcrypt Hash

↓

PostgreSQL

↓

Login Page
```

---

# Database Flow

```
Browser

↓

Route

↓

Service

↓

SQLAlchemy

↓

PostgreSQL

↓

Commit

↓

Response
```

---

# JWT Flow

```
Login

↓

JWT Created

↓

Browser Cookie

↓

Dashboard Request

↓

JWT Validation

↓

Access Granted
```

---

# HTTP Status Codes

| Code | Meaning |
|-------|---------|
| 200 | Success |
| 201 | Created |
| 303 | Redirect |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# Authentication Summary

| Endpoint | Login Required |
|-----------|---------------|
| GET / | ❌ |
| GET /auth/login | ❌ |
| GET /auth/register | ❌ |
| POST /auth/register-form | ❌ |
| POST /auth/register | ❌ |
| POST /auth/login-form | ❌ |
| POST /auth/login | ❌ |
| GET /users/dashboard | ✅ |
| GET /users/profile | ✅ |

---

# Security

Current Security Features

✅ bcrypt Password Hashing

✅ JWT Authentication

✅ HTTPOnly Cookie

✅ Protected Routes

✅ Cache Control

---

# Future APIs

Version 1.1

```
GET /users/profile

GET /users/edit

POST /users/edit
```

Version 1.2

```
POST /users/change-password
```

Version 1.3

```
POST /users/upload-avatar
```

Version 2.0

```
GET /admin/dashboard

GET /admin/users

DELETE /admin/users/{id}

PATCH /admin/users/{id}
```

Version 2.1

```
POST /auth/forgot-password

POST /auth/reset-password
```

---

# API Design Principles

The project follows a layered architecture.

```
Client

↓

Route

↓

Service

↓

Database

↓

Response
```

Business logic is placed inside the Service layer while Routes only handle requests and responses.

---

# Future Improvements

- OAuth Login (Google/GitHub)
- Email Verification
- Refresh Tokens
- Rate Limiting
- User Roles
- Admin APIs
- File Upload APIs
- REST API Versioning
- Docker Deployment APIs

---

# Conclusion

This API documentation provides a complete overview of the endpoints currently implemented in the FastAPI Authentication Platform.

The documentation will continue to evolve as new modules and APIs are added, ensuring that developers, interviewers, and future contributors can easily understand and work with the project.