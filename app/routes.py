from fastapi import APIRouter
from app.models import User
from app import crud

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the FastAPI + MongoDB CRUD app"}

@router.post("/user")
async def add_user(user: User):
    print("Received user:", user)
    return await crud.create_user(user.dict())

@router.get("/users")
async def list_users():
    return await crud.get_users()

@router.get("/user/{email}")
async def get_user(email: str):
    return await crud.get_user_by_email(email)

@router.put("/user/{email}")
async def update_user(email: str, user: User):
    return await crud.update_user(email, user.dict())

@router.delete("/user/{email}")
async def delete_user(email: str):
    return await crud.delete_user(email)
