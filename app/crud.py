from sqlalchemy.orm import Session

from app.models.user import User
from app.security import hash_password


def create_user(
    db: Session,
    email: str,
    username: str,
    password: str,
) -> User:
    user = User(
        email=email,
        username=username,
        password_hash=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
