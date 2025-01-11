from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.api.deps import get_db, get_admin_user
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.services.user_service import UserService

router = APIRouter(
    prefix='/api/v1/users',
    tags=['Users'],
    dependencies=[Depends(get_admin_user)]
)


@router.get(
    '/', 
    response_model=List[UserOut], 
    status_code=status.HTTP_200_OK,
    responses={
        401: {'description': 'Unauthorized'}
    }
)
async def list_users(
    db: Session = Depends(get_db)
) -> List[User]:
    return await UserService.get_all_users(db)


@router.post(
    '/', 
    response_model=UserOut, 
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {'description': 'Invalid credentials'},
        401: {'description': 'Unauthorized'}
    }
)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
) -> User:
    return await UserService.create_user(user, db)


@router.get(
    '/{user_id}', 
    response_model=UserOut, 
    status_code=status.HTTP_200_OK,
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Not found'}
    }
)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return await UserService.get_user_by_id(user_id, db)


@router.patch(
    '/{user_id}', 
    response_model=UserOut, 
    status_code=status.HTTP_200_OK,
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Not found'}
    }
)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
) -> User:
    return await UserService.update_user(db, user_id, user_update)


@router.delete(
    '/{user_id}', 
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Not found'}
    }
)
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    await UserService.delete_user(db, user_id)
