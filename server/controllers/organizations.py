from motor.motor_asyncio import AsyncIOMotorDatabase
from models.organizations import Organization

async def create_organization(db: AsyncIOMotorDatabase, org: Organization):
    existing = await db.organizations.find_one({"name": org.name})
    if existing:
        return None

    org_dict = org.dict(by_alias=True)
    result = await db.organizations.insert_one(org_dict)
    return str(result.inserted_id)
