# FastAPI CSV Retrieval-Augmented Generation (RAG) API

## Overview
This API enables users to upload and query CSV files using Retrieval-Augmented Generation (RAG). The system efficiently stores CSV data along with metadata in a NoSQL database (MongoDB preferred, MySQL optional) and allows users to interact with it via chat. **Postman is used for API testing and interaction.**

## Features
- Accepts CSV files from various sources: Direct file upload, Fetch from a predefined disk location, Pick from a project directory.
- Extracts, indexes, and stores CSV content efficiently.
- Allows querying and chat-based interaction with CSV data.
- Uses open-source LLMs from Hugging Face or APIs from OpenAI/Anthropic.
- Implements robust error handling with proper status codes.

## API Endpoints

### **1. POST /upload** - Upload a CSV file.
**Request:** Multipart/form-data (CSV file) or JSON Body (`{ "file_path": "string" }`)  
**Response:**  
```json
{
    "file_id": "string",
    "message": "Upload successful"
}

