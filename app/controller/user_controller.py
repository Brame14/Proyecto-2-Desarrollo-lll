from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.auth.jwt_handler import get_current_user

from app.model.user import User

from app.service.user_service import UserService

from app.schema.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from app.auth.security import hash_password

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserService()


@router.get(
    "/all",
    response_model=list[UserResponse]
)
def get_all(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return service.list_users(db)


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_by_id(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    user = service.get_user(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.post(
    "/add",
    response_model=UserResponse
)
def add(
        user_data: UserCreate,
        db: Session = Depends(get_db)
):

    user = User(
        username=user_data.username,
        password=hash_password(
            user_data.password
        ),
        role=user_data.role
    )

    return service.create_user(
        db,
        user
    )


@router.put(
    "/update/{user_id}",
    response_model=UserResponse
)
def update(
        user_id: int,
        user_data: UserUpdate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    user = service.get_user(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.username = user_data.username
    user.password = hash_password(
        user_data.password
    )
    user.role = user_data.role

    return service.update_user(
        db,
        user
    )


@router.delete(
    "/delete/{user_id}"
)
def delete(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):

    user = service.get_user(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    service.delete_user(
        db,
        user
    )

    return {
        "message": "User deleted"
    }