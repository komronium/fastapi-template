from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserOut
from app.schemas.auth import LoginRequest, SignupRequest, Token
from app.services.auth_service import AuthService

router = APIRouter(prefix='/api/v1', tags=['Auth'])


@router.post('/login', response_model=Token, status_code=status.HTTP_200_OK)
def login(
    login_request: LoginRequest,
    db: Session = Depends(get_db)
):
    return AuthService.login(db, login_request)


@router.post('/signup', response_model=UserOut, status_code=status.HTTP_200_OK)
def signup(
    signup_request: SignupRequest,
    db: Session = Depends(get_db)
):
    return AuthService.signup(db, signup_request)
