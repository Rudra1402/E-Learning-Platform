from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import ObjectId
from models.users import UserBase

async def create_user(db: AsyncIOMotorDatabase, user: UserBase):
    user_dict = user.dict(by_alias=True)
    user_dict["_id"] = ObjectId(user_dict["_id"])
    if "enrolled_courses" in user_dict:
        user_dict["enrolled_courses"] = [ObjectId(course) for course in user_dict["enrolled_courses"]]
    if "courses_created" in user_dict:
        user_dict["courses_created"] = [ObjectId(course) for course in user_dict["courses_created"]]
    if "organization_id" in user_dict:
        user_dict["organization_id"] = ObjectId(user_dict["organization_id"])
    
    result = await db.users.insert_one(user_dict)
    return result.inserted_id

async def get_user(db: AsyncIOMotorDatabase, email: str):
    user = await db.users.find_one({"email": email})
    if user:
        user["_id"] = str(user["_id"]) 
        return user
    return None
