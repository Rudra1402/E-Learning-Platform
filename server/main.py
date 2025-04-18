from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.organizations import router as organization_router
from routes.users import router as user_router
from database import get_database

app = FastAPI(
    title="E-Learning Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(organization_router, prefix="/api", tags=["Organizations"])
app.include_router(user_router, prefix="/user", tags=["users"])

@app.get("/")
async def root():
    return {"message": "FastAPI with MongoDB connected!"}

@app.get("/getusers")
async def test_db(db=Depends(get_database)):
    collections = await db.list_collection_names()
    print(collections)
    return {"collections": collections}
