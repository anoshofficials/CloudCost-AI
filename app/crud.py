from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
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
def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()
def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()
def update_user(
    db: Session,
    user: User,
    username: str | None = None,
    is_active: bool | None = None,
    role: str | None = None,
) -> User:
    if username is not None:
        user.username = username

    if is_active is not None:
        user.is_active = is_active

    if role is not None:
        user.role = role

    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise

    return user
def deactivate_user(
    db: Session,
    user: User,
) -> User:
    user.is_active = False

    db.commit()
    db.refresh(user)

    return user
