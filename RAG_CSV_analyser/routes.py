from fastapi import APIRouter, UploadFile, File, HTTPException
from database import collection
from models import FileUploadResponse, QueryRequest
import pandas as pd
import io
import uuid

router = APIRouter()


# Endpoint: Upload CSV
@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(file: UploadFile = File(...)):
    try:
        # Read CSV content
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        # Generate unique file ID
        file_id = str(uuid.uuid4())

        # Store file in MongoDB
        collection.insert_one({
            "file_id": file_id,
            "file_name": file.filename,
            "document": df.to_dict(orient="records"),
        })

        return {"file_id": file_id, "message": "Upload successful"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint: List uploaded files
@router.get("/files")
async def list_files():
    try:
        files = list(collection.find({}, {"_id": 0, "file_id": 1, "file_name": 1}))
        return {"files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint: Query CSV data
@router.post("/query")
async def query_csv(request: QueryRequest):
    try:
        file_data = collection.find_one({"file_id": request.file_id}, {"_id": 0, "document": 1})

        if not file_data:
            raise HTTPException(status_code=404, detail="File not found")

        # Convert to DataFrame
        df = pd.DataFrame(file_data["document"])

        # Simple text search (improve with LLM later)
        result = df[df.apply(lambda row: request.query.lower() in row.astype(str).str.lower().to_string(), axis=1)]

        return {"response": result.to_dict(orient="records")}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Endpoint: Delete a file
@router.delete("/file/{file_id}")
async def delete_file(file_id: str):
    try:
        result = collection.delete_one({"file_id": file_id})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="File not found")

        return {"message": "File deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
