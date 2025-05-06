from fastapi import APIRouter, File, UploadFile, HTTPException
import os
from src.services.reader import extract_text_fitz
router = APIRouter()

UPLOAD_DIRECTORY = "uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    print(f"File location: {file_location}")

    with open(file_location, "wb") as f:
        f.write(await file.read())
    text = extract_text_fitz(file_location)
    print(f"Extracted text: {text}")
    # Optionally, you can delete the file after processing
    os.remove(file_location)
    return {text}