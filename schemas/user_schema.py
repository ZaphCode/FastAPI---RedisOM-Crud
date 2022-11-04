from pydantic import BaseModel, EmailStr, Field, PositiveInt

class UserSch(BaseModel):
    username: str = Field(..., min_length=5, max_length=15, example='John Doe')
    email: EmailStr
    age: PositiveInt = Field(..., example=18)
    password: str = Field(..., min_length=8, example='password123')
    