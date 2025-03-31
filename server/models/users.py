from pydantic import BaseModel, EmailStr, Field
from typing import List
import uuid
from bson import ObjectId

class PyObjectId(str):
    """Ensures the field is always stored as a valid MongoDB ObjectID string."""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectID format")
        return str(v)

class UserRole:
    STUDENT = 1
    INSTRUCTOR = 2
    ORG_ADMIN = 3
    SUPER_ADMIN = 5

class UserBase(BaseModel):
    id: PyObjectId = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    email: EmailStr
    name: str
    role: int 
    is_active: bool = True

class Student(UserBase):
    role: int = UserRole.STUDENT
    enrolled_courses: List[PyObjectId] = [] 

class Instructor(UserBase):
    role: int = UserRole.INSTRUCTOR
    courses_created: List[PyObjectId] = [] 

class OrgAdmin(UserBase):
    role: int = UserRole.ORG_ADMIN
    organization_id: PyObjectId 

class SuperAdmin(UserBase):
    role: int = UserRole.SUPER_ADMIN
