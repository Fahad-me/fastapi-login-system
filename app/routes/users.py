from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_access_token
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

templates = Jinja2Templates(
    directory="app/templates"
)


# -----------------------------
# Dashboard
# -----------------------------
@router.get(
    "/dashboard",
    response_class=HTMLResponse
)
def dashboard(
    request: Request,
    db: Session = Depends(get_db)
):

    # Read JWT from cookie
    token = request.cookies.get("access_token")

    if not token:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    # Decode JWT
    payload = decode_access_token(token)

    if not payload:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    email = payload.get("sub")

    if not email:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    # Find user
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    response = templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user
        }
    )

    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response


# -----------------------------
# Profile
# -----------------------------
@router.get(
    "/profile",
    response_class=HTMLResponse
)
def profile(
    request: Request,
    db: Session = Depends(get_db)
):

    token = request.cookies.get("access_token")

    if not token:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    payload = decode_access_token(token)

    if not payload:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    email = payload.get("sub")

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    response = templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": user
        }
    )

    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response