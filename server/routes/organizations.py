from fastapi import APIRouter, Depends, HTTPException, status
from database import get_database
from models.organizations import Organization
from controllers.organizations import create_organization
from pymongo.errors import PyMongoError

router = APIRouter()

@router.post("/organizations", response_model=dict)
async def add_organization(org: Organization, db=Depends(get_database)):
    try:
        org_id = await create_organization(db, org)
        if not org_id:
            raise HTTPException(status_code=400, detail="Organization already exists")

        return {"message": "Organization added successfully", "id": org_id, "org": org}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")

    except PyMongoError:
        raise HTTPException(status_code=500, detail="Database operation failed")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
