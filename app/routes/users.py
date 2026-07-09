from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/profile")
def get_profile():
    return {
        "message": "Profile endpoint (Coming Soon)"
    }


@router.get("/dashboard")
def dashboard():
    return {
        "message": "Welcome to your dashboard!"
    }