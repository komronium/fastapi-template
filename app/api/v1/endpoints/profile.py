from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserOut, UserUpdate
from app.api.deps import get_db, get_current_user
from app.services.user_service import UserService

router = APIRouter(
    prefix='/api/v1/profile',
    tags=['Profile']
)


@router.get(
    '/',
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Not found'}
    }
)
async def get_profile(
    current_user: User = Depends(get_current_user)
) -> User:
    return current_user


@router.patch(
    '/',
    response_model=UserOut,
    status_code=status.HTTP_200_OK,
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Not found'}
    }
)
async def update_profile(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> User:
    return await UserService.update_user(db, current_user.id, user_update)


@router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        401: {'description': 'Unauthorized'},
        404: {'description': 'Not found'}
    }
)
async def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> None:
    await UserService.delete_user(db, current_user.id)
