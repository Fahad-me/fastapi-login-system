# 🐞 FastAPI Authentication Platform

# Bugs and Solutions

---

# About This Document

This document records every bug, issue, error, and challenge encountered during the development of the FastAPI Authentication Platform.

The purpose is to:

- Keep a history of solved problems
- Help future debugging
- Improve development skills
- Prepare for technical interviews
- Document project decisions

---

# Bug #1

## Problem

User registration was successful from the frontend, but no user record appeared inside PostgreSQL.

---

## Symptoms

- Registration page opened successfully.
- No error was shown.
- PostgreSQL table remained empty.
- pgAdmin displayed zero users.

---

## Root Cause

The HTML registration form submitted data to the wrong endpoint.

The HTML form used:

```
POST /auth/register
```

But the HTML form sends data using `application/x-www-form-urlencoded`, while `/auth/register` expected a JSON request body (`UserCreate` schema).

As a result, the request never reached the registration logic correctly.

---

## Solution

A dedicated HTML endpoint was created:

```
POST /auth/register-form
```

Inside this endpoint:

- Receive data using `Form(...)`
- Convert it into `UserCreate`
- Call `register_user()`
- Redirect user to Login page

---

## Files Modified

- app/routes/auth.py

---

## Learning

HTML Forms and JSON APIs are different.

FastAPI provides `Form()` specifically for HTML form submissions.

---

# Bug #2

## Problem

Login page authenticated successfully, but dashboard did not know who the logged-in user was.

---

## Symptoms

Dashboard always displayed:

```
User

user@example.com
```

instead of actual user information.

---

## Root Cause

The JWT token was created but never stored in the browser.

Without the token, the dashboard could not identify the current user.

---

## Solution

Store the JWT inside an HTTP-only cookie.

```
response.set_cookie(
    key="access_token",
    value=token["access_token"],
    httponly=True
)
```

Then read the cookie in protected routes.

---

## Files Modified

- app/routes/auth.py

---

## Learning

JWT authentication requires:

User Login

↓

JWT Token

↓

Browser Cookie

↓

Protected Route

---

# Bug #3

## Problem

After clicking Logout, pressing the browser Back button opened the dashboard again.

---

## Symptoms

Logout appeared successful.

Browser Back button reopened dashboard.

---

## Root Cause

The browser cached the dashboard page.

The dashboard HTML remained inside browser memory.

---

## Solution

Disable caching.

```
Cache-Control

no-store

no-cache

must-revalidate
```

Also add:

```
Pragma: no-cache

Expires: 0
```

---

## Files Modified

- app/routes/users.py

---

## Learning

Logout alone is not enough.

Protected pages should disable browser caching.

---

# Bug #4

## Problem

Home button always opened Login page.

---

## Symptoms

Navigation:

Home

↓

Login page

instead of Home page.

---

## Root Cause

Navbar contained:

```
href="/auth/login"
```

instead of

```
href="/"
```

---

## Solution

Update navigation links.

---

## Files Modified

- app/templates/base.html

---

## Learning

Always verify navigation after adding new pages.

---

# Bug #5

## Problem

Dashboard route returned JSON instead of HTML.

---

## Symptoms

Browser displayed:

```
{
    "message":"Welcome..."
}
```

instead of dashboard page.

---

## Root Cause

Dashboard endpoint returned a Python dictionary.

---

## Solution

Render HTML using:

```
TemplateResponse()
```

---

## Files Modified

- app/routes/users.py

---

## Learning

FastAPI supports:

- JSON APIs
- HTML Pages

Use the correct response type.

---

# Bug #6

## Problem

Home page looked identical to Login page.

---

## Symptoms

Opening

```
/
```

showed Login page.

---

## Root Cause

main.py rendered:

```
login.html
```

instead of

```
home.html
```

---

## Solution

Create dedicated homepage.

```
home.html
```

Update Home route.

---

## Files Modified

- app/main.py

- app/templates/home.html

---

## Learning

Landing pages and Login pages should be separate.

---

# Bug #7

## Problem

Git detected Python cache files.

---

## Symptoms

git status

displayed:

```
__pycache__/

*.pyc
```

---

## Root Cause

Python automatically creates cache files.

Git tracked them.

---

## Solution

Create:

```
.gitignore
```

Ignore:

```
__pycache__/

*.pyc
```

Remove cached files:

```
git rm -r --cached app/__pycache__

git rm -r --cached app/routes/__pycache__
```

---

## Learning

Cache files should never be committed.

---

# Bug #8

## Problem

User expected PostgreSQL table to update automatically.

---

## Symptoms

New users were not visible immediately.

---

## Root Cause

pgAdmin needed table refresh.

---

## Solution

Refresh table manually or run:

```
SELECT * FROM users;
```

---

## Learning

Database GUIs do not always auto-refresh.

---

# Bug #9

## Problem

Navbar design looked outdated.

---

## Symptoms

Flat design.

No hover animation.

Weak spacing.

---

## Solution

Redesign navbar using:

- Glassmorphism
- Sticky Navigation
- Hover Underline
- Better Responsive Layout

---

## Files Modified

- style.css

---

# Bug #10

## Problem

Homepage lacked a professional appearance.

---

## Solution

Created:

- Hero Section
- Feature Cards
- Footer
- Animations
- Floating Background
- Responsive Design

---

## Files Modified

- home.html

- style.css

---

# Current Status

✔ All reported issues resolved.

---

# Future Bugs

This document will continue to grow as the project develops.

Upcoming sections:

- Profile Bugs
- Password Reset Bugs
- Admin Panel Bugs
- Email Bugs
- Deployment Bugs
- Docker Issues
- Railway/Render Deployment Issues
- Security Improvements

---

# Final Learning

Every bug solved is a learning opportunity.

A successful software engineer is not someone who never encounters bugs.

A successful software engineer is someone who understands why the bug occurred, identifies the root cause, implements the correct solution, and documents the fix for future reference.