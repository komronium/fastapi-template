import uuid
import boto3
from typing import List
from botocore.exceptions import ClientError
from fastapi import UploadFile, HTTPException
from app.core.config import settings


class StorageService:
    ALLOWED_EXTENSIONS: List[str] = ['jpg', 'jpeg', 'png', 'gif']
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5 MB

    @staticmethod
    def _get_s3_client() -> boto3.client:
        return boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY.get_secret_value(),
            region_name=settings.AWS_S3_REGION
        )

    @staticmethod
    def _get_file_extension(file: UploadFile) -> str:
        return file.content_type.split('/')[-1].lower()

    @staticmethod
    def _validate_file(file: UploadFile) -> None:
        if not file.filename:
            raise HTTPException(status_code=400, detail='No filename provided')

        ext = StorageService._get_file_extension(file)
        if ext not in StorageService.ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail='Invalid file type')

    @staticmethod
    async def upload_file(file: UploadFile, folder: str) -> str:
        StorageService._validate_file(file)

        try:
            ext = StorageService._get_file_extension(file)
            key = f"{folder}/{uuid.uuid4()}.{ext}"
            s3_client = StorageService._get_s3_client()

            s3_client.upload_fileobj(
                file.file,
                settings.AWS_STORAGE_BUCKET_NAME,
                key,
                ExtraArgs={'ACL': 'public-read'}
            )

            return StorageService.get_file_url(key)
        except ClientError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to upload file: {str(e)}"
            )

    @staticmethod
    async def delete_file(file_url: str) -> None:
        if not file_url:
            return

        try:
            key = file_url.split(f"{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/")[1]
            s3_client = StorageService._get_s3_client()
            s3_client.delete_object(
                Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                Key=key
            )
        except (ClientError, IndexError):
            pass

    @staticmethod
    def get_file_url(key: str) -> str:
        return f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{key}"
