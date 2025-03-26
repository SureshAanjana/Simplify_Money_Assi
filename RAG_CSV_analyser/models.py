from pydantic import BaseModel

# Model for file upload response
class FileUploadResponse(BaseModel):
    file_id: str
    message: str

# Model for querying CSV data
class QueryRequest(BaseModel):
    file_id: str
    query: str
