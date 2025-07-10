from fastapi import FastAPI
from app.models import User
from app import crud

app = FastAPI()

@app.post("/user")
async def add_user(user: User):
    return await crud.create_user(user.dict())

@app.get("/users")
async def list_users():
    return await crud.get_users()

@app.get("/user/{email}")
async def get_user(email: str):
    return await crud.get_user_by_email(email)

@app.put("/user/{email}")
async def update_user(email: str, user: User):
    return await crud.update_user(email, user.dict())

@app.delete("/user/{email}")
async def delete_user(email: str):
    return await crud.delete_user(email)
