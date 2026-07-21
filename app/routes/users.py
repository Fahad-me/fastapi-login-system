from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.user_service import (
    get_current_user,
    update_user_profile
)
    

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

    user = get_current_user(db, token)

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

    user = get_current_user(db, token)

    if not user:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    response = templates.TemplateResponse(
        "profile.html",
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
# Edit Profile
# -----------------------------
@router.get(
    "/edit-profile",
    response_class=HTMLResponse
)
def edit_profile(
    request: Request,
    db: Session = Depends(get_db)
):

    token = request.cookies.get("access_token")

    if not token:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    user = get_current_user(db, token)

    if not user:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    response = templates.TemplateResponse(
        "edit_profile.html",
        {
            "request": request,
            "user": user
        }
    )

    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response

@router.post("/edit-profile")
def update_profile(
    request: Request,
    full_name: str = Form(...),
    username: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db)
):

    token = request.cookies.get("access_token")

    if not token:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    user = get_current_user(db, token)

    if not user:
        return RedirectResponse(
            url="/auth/login",
            status_code=303
        )

    try:
        update_user_profile(
            db=db,
            user=user,
            full_name=full_name,
            username=username,
            email=email
        )

    except ValueError as e:
        return templates.TemplateResponse(
            "edit_profile.html",
            {
                "request": request,
                "user": user,
                "error": str(e)
            }
        )

    return RedirectResponse(
        url="/users/profile",
        status_code=303
    )