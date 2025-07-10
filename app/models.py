from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr  # ✅ This triggers email format validation
