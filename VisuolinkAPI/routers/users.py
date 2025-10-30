from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy import or_, and_, update
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from VisuolinkAPI.utils import hashPassword, verify_password
from VisuolinkAPI.database import get_db
from VisuolinkAPI.models import User, Usernames
from VisuolinkAPI.schema import CreateUserSchema, GetUserSchema, ChangePasswordSchema, GetUsernamesSchema, RequestCredentialSchema, UpdateUserSchema


router = APIRouter(prefix="/users", tags=["User"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[GetUsernamesSchema])
def get_usernames(db: Session = Depends(get_db)):
    usernames_list = db.execute(select(Usernames.username)).scalars().all()
    return [GetUsernamesSchema(username=u) for u in usernames_list]


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=GetUserSchema)
def get_user_info(id: int, db: Session = Depends(get_db)):

    user = db.execute(select(User).where(User.id == id)).scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed to fetch Information! No such user id exits ")
    
    return GetUserSchema(username=user.username, name=user.name, email=user.email, phone=user.phone)


@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_model=GetUserSchema)
def update_user_info(data: UpdateUserSchema, db: Session = Depends(get_db)):

    user_data = db.execute(select(User).where(User.username == data.oldUsername)).scalar_one_or_none()

    if user_data is None or not verify_password(data.password, user_data.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    existing_email = db.execute(select(User).where(and_(User.id != user_data.id, User.email == data.email))).scalar_one_or_none()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email already exists")
    
    user_data.username, user_data.name, user_data.email, user_data.phone = data.username, data.name, data.email, data.phone
    db.execute(update(Usernames).where(Usernames.id == user_data.id).values(username=user_data.username))
    try:
        db.commit()
        db.refresh(user_data)
        return GetUserSchema(username=user_data.username, name=user_data.name, email=user_data.email, phone=user_data.phone)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to update profile — possible duplicate record."
        )


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user_new: CreateUserSchema, db: Session = Depends(get_db)):
    existing_user = db.execute(select(User).where(or_(User.username == user_new.username, User.email == user_new.email))).scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email already exists")
    
    new_user = User(username=user_new.username, password=hashPassword(user_new.password), name=user_new.name, email=user_new.email, phone=user_new.phone)
    db.add(new_user)
    db.add(Usernames(username=new_user.username))

    try:
        db.commit()
        db.refresh(new_user)
        return {"status": "success", "message": "Profile created.", "user_id": new_user.id}
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to create profile — possible duplicate record."
        )


@router.put("/cp", status_code=status.HTTP_202_ACCEPTED)
def change_password(body: ChangePasswordSchema, db: Session = Depends(get_db)):
    user_data = db.execute(select(User).where(User.username == body.username)).scalar_one_or_none()

    if user_data is None or not verify_password(body.password, user_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    user_data.password = hashPassword(body.newPassword)

    try:
        db.commit()
        return {"status": "success", "message": "Password Changed Successfully."}
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to change password — possible connection error."
        )


@router.post("/auth/login", status_code=status.HTTP_200_OK)
def login(body: RequestCredentialSchema, db: Session = Depends(get_db)):
    user_data = db.execute(select(User).where(User.username == body.username)).scalar_one_or_none()

    if user_data is None or not verify_password(body.password, user_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    return {"id": user_data.id, "username": user_data.username}
