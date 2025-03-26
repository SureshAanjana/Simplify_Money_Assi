from pymongo import MongoClient
import os
import urllib.parse

# Encode username and password
username = urllib.parse.quote_plus("suresh")  # Your MongoDB username
password = urllib.parse.quote_plus("Suresh@2003")  # Your MongoDB password

# MongoDB connection string with encoded credentials
MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.f8lenod.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(MONGO_URI)

# Select database and collection
db = client["rag_csv_db"]
collection = db["csv_files"]

# Test the connection
if __name__ == "__main__":
    print("Connected to MongoDB successfully!")
    print(f"Database: {db.name}")
    print(f"Collection: {collection.name}")
