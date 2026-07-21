from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import decode_access_token


# -----------------------------
# Get User By Email
# -----------------------------
def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

# -----------------------------
# Get User By Username
# -----------------------------
def get_user_by_username(
    db: Session,
    username: str
):

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

# -----------------------------
# Get User By ID
# -----------------------------
def get_user_by_id(
    db: Session,
    user_id: int
):

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )




# -----------------------------
# Get Current User
# -----------------------------
def get_current_user(
    db: Session,
    token: str
):

    payload = decode_access_token(token)

    if not payload:
        return None

    email = payload.get("sub")

    if not email:
        return None

    return get_user_by_email(
        db,
        email
    )

# -----------------------------
# Update User Profile
# -----------------------------
def update_user_profile(
    db: Session,
    user: User,
    full_name: str,
    username: str,
    email: str
):

    full_name = full_name.strip()
    username = username.strip()
    email = email.strip().lower()

    # Check username
    existing_username = get_user_by_username(db, username)

    if existing_username and existing_username.id != user.id:
        raise ValueError("Username already exists.")

    # Check email
    existing_email = get_user_by_email(db, email)

    if existing_email and existing_email.id != user.id:
        raise ValueError("Email already exists.")

    user.full_name = full_name
    user.username = username
    user.email = email

    db.commit()
    db.refresh(user)

    return user


