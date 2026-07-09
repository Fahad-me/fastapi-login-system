from fastapi import (
    APIRouter,
    Depends,
    Request,
    status,
    Form
)
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
    Token,
)
from app.services.auth_service import (
    register_user,
    authenticate_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

templates = Jinja2Templates(
    directory="app/templates"
)

# ----------------------------------------
# Login Page
# ----------------------------------------
@router.get(
    "/login",
    response_class=HTMLResponse
)
def login_page(request: Request):

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "title": "Login"
        }
    )


# ----------------------------------------
# Register Page
# ----------------------------------------
@router.get(
    "/register",
    response_class=HTMLResponse
)
def register_page(request: Request):

    return templates.TemplateResponse(
        "register.html",
        {
            "request": request,
            "title": "Register"
        }
    )


# ----------------------------------------
# Swagger API Register
# ----------------------------------------
@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return register_user(db, user)


# ----------------------------------------
# HTML Register
# ----------------------------------------
@router.post("/register-form")
def register_form(
    full_name: str = Form(...),
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    user = UserCreate(
        full_name=full_name,
        username=username,
        email=email,
        password=password,
    )

    register_user(db, user)

    return RedirectResponse(
        url="/auth/login",
        status_code=303
    )


# ----------------------------------------
# Swagger API Login
# ----------------------------------------
@router.post(
    "/login",
    response_model=Token
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return authenticate_user(db, user)


# ----------------------------------------
# HTML Login
# ----------------------------------------
@router.post("/login-form")
def login_form(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):

    user = UserLogin(
        email=email,
        password=password
    )

    token = authenticate_user(
        db,
        user
    )

    response = RedirectResponse(
        url="/users/dashboard",
        status_code=303
    )

    response.set_cookie(
        key="access_token",
        value=token["access_token"],
        httponly=True,
        samesite="lax"
    )

    return response


# ----------------------------------------
# Logout
# ----------------------------------------
@router.get("/logout")
def logout():

    response = RedirectResponse(
        url="/auth/login",
        status_code=303
    )

    # Delete JWT Cookie
    response.delete_cookie("access_token")

    return response