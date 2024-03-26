from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=1, lt=130)
    email: EmailStr
    password: str = Field(min_length=8, max_length=24)
