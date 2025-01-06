from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserOut, UserUpdate
from app.api.deps import get_db, get_current_user
from app.services.user_service import UserService

router = APIRouter(prefix='/api/v1/profile', tags=['Profile'])


@router.get('/', response_model=UserOut, status_code=200)
async def get_profile(
    current_user: User = Depends(get_current_user)
):
    return current_user


@router.put('/', response_model=UserOut, status_code=200)
async def update_profile(
    update_request: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await UserService.update_user(db, current_user.id, update_request)


@router.delete('/', status_code=204)
async def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await UserService.delete_user(db, current_user.id)
