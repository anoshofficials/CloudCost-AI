from app.auth import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse
from app.security import verify_password

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.auth import create_access_token, get_current_user_email

from app.config import settings
from app.crud import create_user, get_user, get_user_by_email, get_users
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.auth import create_access_token, get_current_user_email
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered FinOps platform for multi-cloud cost monitoring and optimization.",
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running!"
    }



@app.post("/auth/login", response_model=TokenResponse)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
):
    user = get_user_by_email(db, credentials.email)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    if not verify_password(credentials.password, user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
    }


@app.post("/users", response_model=UserResponse)
def create_user_api(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered",
        )

    return create_user(
        db,
        email=user.email,
        username=user.username,
        password=user.password,
    )

@app.get("/users/me", response_model=UserResponse)
def get_current_user(
    email: str = Depends(get_current_user_email),
    db: Session = Depends(get_db),
):
    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user_api(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user

@app.get("/users", response_model=list[UserResponse])
def list_users(
   skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return get_users(db, skip=skip, limit=limit)
