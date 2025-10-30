from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from VisuolinkAPI.database import engine
from VisuolinkAPI.routers import users
from VisuolinkAPI import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
def home():
    informations = {
        "API Name": "Visolink API",
        "Description": "This is an API for Visuolink Applications for authentication and autorization at anytime",
        "Endpoints": "/, /users, /email",
        "API Documenation": "/docs",
        "Version": "1.08",
        "Created By": "Sumit Dubey",
        "Contact": "sumitdubey810@outlook.com",
        "Tools used": {
            "Backend": "FastAPI",
            "Database": "PostgreSQL",
            "IDE": "VS Code"
        }
    }

    return JSONResponse(content=informations, status_code=200)

app.include_router(users.router)

