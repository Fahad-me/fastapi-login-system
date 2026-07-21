# 💼 FastAPI Authentication Platform

# Interview Notes

---

# About This Document

This document contains interview questions and answers based on the FastAPI Authentication Platform project.

The purpose of this document is to prepare for:

- Campus Placements
- Technical Interviews
- HR Discussions
- Project Demonstrations
- College Viva
- Internship Interviews

Every question is answered from the perspective of this project.

---

# SECTION 1

# Project Introduction

---

## Q1. Tell me about your project.

Answer:

My project is called **FastAPI Authentication Platform**.

It is a secure authentication system developed using FastAPI.

The platform allows users to register, login, authenticate using JWT tokens, and access protected dashboard pages.

User information is stored securely inside PostgreSQL while passwords are encrypted using bcrypt hashing.

The frontend is built using HTML, CSS, JavaScript, and Jinja2 templates.

The project follows a modular architecture using Models, Schemas, Services, Routes, Templates, and Static files.

---

## Q2. Why did you choose FastAPI?

Answer:

FastAPI provides:

- High Performance

- Automatic API Documentation

- Data Validation using Pydantic

- Easy Integration with SQLAlchemy

- JWT Authentication Support

- Asynchronous Programming Support

Compared to traditional frameworks, FastAPI is faster and easier to develop REST APIs.

---

## Q3. What problem does your project solve?

Answer:

The project demonstrates how to build a secure authentication platform.

Instead of storing passwords in plain text, passwords are encrypted.

Instead of allowing unrestricted access, protected routes require authentication.

This improves application security.

---

## Q4. What are the main features?

Answer:

Current Features

- User Registration

- User Login

- JWT Authentication

- PostgreSQL Database

- Password Hashing

- Protected Dashboard

- Responsive UI

Upcoming Features

- Profile

- Change Password

- Forgot Password

- Admin Dashboard

---

# SECTION 2

# FastAPI

---

## Q5. What is FastAPI?

Answer:

FastAPI is a modern Python web framework used to build REST APIs.

It is based on ASGI and Starlette.

It uses Pydantic for data validation.

---

## Q6. Why FastAPI instead of Flask?

Answer:

FastAPI provides:

- Better Performance

- Automatic Swagger Documentation

- Type Validation

- Async Support

- Cleaner Development

Flask requires additional libraries for many of these features.

---

## Q7. What is APIRouter?

Answer:

APIRouter helps organize endpoints.

Instead of writing every endpoint inside main.py, endpoints are separated into multiple route files.

Example:

auth.py

users.py

admin.py

This improves project organization.

---

## Q8. Why keep business logic inside services?

Answer:

Routes should only receive requests and return responses.

Business logic belongs inside the Service layer.

Advantages:

- Clean Code

- Reusable Functions

- Easy Testing

- Better Maintenance

---

# SECTION 3

# PostgreSQL

---

## Q9. Why PostgreSQL?

Answer:

PostgreSQL is:

- Open Source

- Reliable

- ACID Compliant

- Secure

- Scalable

It is widely used in production systems.

---

## Q10. Why not SQLite?

Answer:

SQLite is suitable for small applications.

PostgreSQL supports:

- Multiple Users

- Better Performance

- Scalability

- Production Deployment

---

## Q11. How did you connect PostgreSQL?

Answer:

Connection is established using SQLAlchemy Engine.

Database URL:

postgresql://username:password@localhost/database

SQLAlchemy manages the connection.

---

# SECTION 4

# SQLAlchemy

---

## Q12. What is SQLAlchemy?

Answer:

SQLAlchemy is an ORM (Object Relational Mapper).

It converts Python objects into database records.

Instead of writing SQL manually:

User()

db.add(user)

db.commit()

---

## Q13. Why ORM?

Answer:

Advantages:

- Less SQL

- Cleaner Code

- Database Independence

- Easier Maintenance

---

# SECTION 5

# Authentication

---

## Q14. What is JWT?

Answer:

JWT stands for JSON Web Token.

It is a secure token used for authentication.

The server creates the token after login.

The client sends the token with every request.

The server verifies the token before allowing access.

---

## Q15. Why JWT instead of Sessions?

Answer:

JWT

- Stateless

- Faster

- Better for APIs

- Scalable

Sessions require server-side storage.

---

## Q16. Why bcrypt?

Answer:

Passwords should never be stored in plain text.

bcrypt converts passwords into secure hashes.

Even database administrators cannot see original passwords.

---

## Q17. Explain Login Flow.

Answer:

User enters email and password.

↓

FastAPI receives request.

↓

Database checks email.

↓

Password verified using bcrypt.

↓

JWT Token generated.

↓

Cookie stored.

↓

Dashboard opened.

---

## Q18. Explain Register Flow.

Answer:

User submits registration form.

↓

Validation using Pydantic.

↓

Password hashed.

↓

User stored inside PostgreSQL.

↓

Redirect to Login.

---

# SECTION 6

# HTML & Jinja

---

## Q19. Why Jinja2?

Answer:

Jinja2 allows dynamic HTML rendering.

Instead of writing static HTML, Python data can be displayed directly.

Example:

{{ user.full_name }}

---

## Q20. Why TemplateResponse?

Answer:

TemplateResponse renders HTML templates from FastAPI.

---

# SECTION 7

# Git & GitHub

---

## Q21. Why Git?

Answer:

Git tracks project history.

Allows rollback.

Supports collaboration.

Provides version control.

---

## Q22. Why GitHub?

Answer:

GitHub hosts Git repositories online.

Allows backup.

Portfolio showcase.

Team collaboration.

---

# SECTION 8

# Security

---

## Q23. Why Hash Passwords?

Answer:

Plain text passwords are insecure.

Hashing protects user credentials.

---

## Q24. What happens if JWT expires?

Answer:

The user must login again or refresh the token if refresh tokens are implemented.

---

# SECTION 9

# Future Improvements

---

Future Features

- Email Verification

- Forgot Password

- Refresh Tokens

- Profile Picture

- Admin Dashboard

- User Roles

- Docker

- Redis

- CI/CD

- Deployment

---

# HR Questions

Why did you build this project?

What challenges did you face?

What was the hardest part?

What did you learn?

What would you improve?

Why FastAPI?

Why PostgreSQL?

Why JWT?

---

# Personal Notes

This document will continue to grow as the project develops.

Every completed feature will add new interview questions and answers.