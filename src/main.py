from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.upload import router as upload_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF upload API!"}