from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from pymongo.errors import PyMongoError
from database import get_database, user_exists
from models.users import Student, Instructor, OrgAdmin, SuperAdmin, UserRole
from controllers.users import create_user

router = APIRouter()

@router.post("/register/student")
async def register_student(student: Student, db=Depends(get_database)):
    try:
        if await user_exists(db, student.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

        student.role = UserRole.STUDENT
        student.enrolled_courses = [ObjectId(course) for course in student.enrolled_courses]
        
        student_id = await create_user(db, student)
        return {"message": "Student registered successfully", "id": str(student_id), "student": student}
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid input: {str(e)}"
        )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@router.post("/register/instructor")
async def register_instructor(instructor: Instructor, db=Depends(get_database)):
    try:
        if await user_exists(db, instructor.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

        instructor.role = UserRole.INSTRUCTOR
        instructor.courses_created = [ObjectId(course) for course in instructor.courses_created]
        
        instructor_id = await create_user(db, instructor)
        return {"message": "Instructor registered successfully", "id": str(instructor_id), "instructor": instructor}
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid input: {str(e)}"
        )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@router.post("/register/admin")
async def register_org_admin(org_admin: OrgAdmin, db=Depends(get_database)):
    try:
        if await user_exists(db, org_admin.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

        org_admin.role = UserRole.ORG_ADMIN
        org_admin.organization_id = ObjectId(org_admin.organization_id)
        
        admin_id = await create_user(db, org_admin)
        return {"message": "Organization Admin registered successfully", "id": str(admin_id), "admin": org_admin}
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid input: {str(e)}"
        )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@router.post("/register/super-admin")
async def register_super_admin(super_admin: SuperAdmin, db=Depends(get_database)):
    try:
        super_admin.role = UserRole.SUPER_ADMIN        
        super_admin_id = await create_user(db, super_admin)
        return {"message": "Super Admin registered successfully", "id": str(super_admin_id)}
    
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid input: {str(e)}"
        )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred: {str(e)}"
        )
