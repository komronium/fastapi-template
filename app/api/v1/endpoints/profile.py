from fastapi import APIRouter, Depends, UploadFile, File, status
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserOut, UserUpdate
from app.api.deps import get_db, get_current_user
from app.services.user_service import UserService

router = APIRouter(prefix='/api/v1/profile', tags=['Profile'])


@router.get('/', response_model=UserOut, status_code=status.HTTP_200_OK)
async def get_profile(
    current_user: User = Depends(get_current_user)
):
    return current_user


@router.put('/', response_model=UserOut, status_code=status.HTTP_200_OK)
async def update_profile(
    update_request: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await UserService.update_user(db, current_user.id, update_request)


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    await UserService.delete_user(db, current_user.id)


@router.post('/image', response_model=UserOut, status_code=status.HTTP_200_OK)
async def upload_profile_image(
        file: UploadFile = File(...),
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return await UserService.update_profile_image(db, current_user.id, file)


@router.delete('/image', response_model=UserOut, status_code=status.HTTP_200_OK)
async def remove_profile_image(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return await UserService.remove_profile_image(db, current_user.id)
