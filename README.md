FastAPI CSV Retrieval-Augmented Generation (RAG) API

Overview

This API enables users to upload and query CSV files using Retrieval-Augmented Generation (RAG). The system efficiently stores CSV data along with metadata in a NoSQL database (MongoDB preferred, MySQL optional) and allows users to interact with it via chat.

Features

Accepts CSV files from various sources:

Direct file upload.

Fetch from a predefined disk location.

Pick from a project directory.

Extracts, indexes, and stores CSV content.

Allows querying and chat-based interaction with the CSV data.

Uses open-source LLMs from Hugging Face or APIs from OpenAI/Anthropic.

Implements robust error handling with proper status codes.

Uses Postman for API testing and interaction.

API Endpoints

POST /upload

Description: Upload a CSV file.

Input:

Multipart/form-data: CSV file

JSON Body (Alternative): { "file_path": "string" }

Output:

{
    "file_id": "string",
    "message": "Upload successful"
}

Errors:

400 Bad Request - Invalid file format.

500 Internal Server Error - Storage failure.

GET /files

Description: Retrieve a list of uploaded files.

Input: None

Output:

{
    "files": [
        { "file_id": "string", "file_name": "string" }
    ]
}

Errors:

500 Internal Server Error - Retrieval failure.

POST /query

Description: Query a CSV file by file ID and search term.

Input:

{
    "file_id": "string",
    "query": "string"
}

Output:

{
    "response": "string"
}

Errors:

400 Bad Request - Missing parameters.

404 Not Found - File not found.

DELETE /file/{file_id}

Description: Delete a CSV file.

Input: File ID as a URL parameter.

Output:

{
    "message": "File deleted successfully"
}

Errors:

404 Not Found - File does not exist.

500 Internal Server Error - Deletion failure.

Data Schema

Field

Type

Description

file_id

String

Unique identifier for the uploaded file

file_name

String

Original file name

document

Object

CSV content stored in an indexable format
