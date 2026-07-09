from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.database import Base, engine
from app.models.user import User
from app.routes import auth, users

# ------------------------------------
# Create Database Tables
# ------------------------------------
Base.metadata.create_all(bind=engine)

# ------------------------------------
# FastAPI Application
# ------------------------------------
app = FastAPI(
    title="FastAPI Login System",
    description="A complete authentication system built with FastAPI",
    version="1.0.0"
)

# ------------------------------------
# Static Files
# ------------------------------------
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# ------------------------------------
# Templates
# ------------------------------------
templates = Jinja2Templates(
    directory="app/templates"
)

# ------------------------------------
# Register Routers
# ------------------------------------
app.include_router(auth.router)
app.include_router(users.router)

# ------------------------------------
# Home Page
# ------------------------------------
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "title": "Home"
        }
    )
# ------------------------------------
# Health Check
# ------------------------------------
@app.get("/health")
def health():
    return {
        "status": "OK",
        "application": "FastAPI Login System"
    }