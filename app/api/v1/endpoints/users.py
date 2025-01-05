from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService

router = APIRouter(prefix='/api/v1/users')


@router.get('/', response_model=List[UserOut])
async def get_all_users(db: Session = Depends(get_db)):
    return await UserService.get_all_users(db)


@router.post('/', response_model=UserOut)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return await UserService.create_user(user, db)


@router.get('/{user_id}', response_model=UserOut)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return await UserService.get_user_by_id(user_id, db)
