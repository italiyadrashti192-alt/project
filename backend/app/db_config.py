from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGODB_URL:
    raise ValueError("MONGODB_URL is not found in .env")

if not DATABASE_NAME:
    raise ValueError("DATABASE_NAME is not found in .env")


# Create client
client = MongoClient(
    MONGODB_URL,
    serverSelectionTimeoutMS=5000
)

# Database object
db = client[DATABASE_NAME]


# Function to test connection
def check_database_connection():
    try:
        client.admin.command("ping")
        return True, "MongoDB Atlas Connected Successfully!"

    except Exception as e:
        return False, str(e)


# Test connection when backend starts
connected, message = check_database_connection()

if connected:
    print("✅", message)
    print(f"📁 Database: {DATABASE_NAME}")
else:
    print("❌ MongoDB Connection Failed!")
    print("Error:", message)


# import os

# from dotenv import load_dotenv
# from pymongo import MongoClient
# from pymongo.errors import PyMongoError


# # Load environment variables from .env
# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")

# if not MONGO_URI:
#     raise RuntimeError(
#         "MONGO_URI is missing. Please add MONGO_URI to your .env file."
#     )


# # Create MongoDB client.
# # Do NOT authenticate/change password here.
# client = MongoClient(
#     MONGO_URI,
#     serverSelectionTimeoutMS=5000,
# )


# # Get database from the MongoDB URI
# db = client.get_default_database()


# def check_mongodb():
#     """
#     Check whether MongoDB is available.

#     Returns:
#         True  -> MongoDB is connected
#         False -> MongoDB is unavailable
#     """
#     try:
#         client.admin.command("ping")
#         print("✅ MongoDB Connected Successfully!")
#         return True

#     except PyMongoError as e:
#         print("❌ MongoDB Connection Failed!")
#         print(f"Error: {e}")
#         return False


# def get_database():
#     """
#     Return the MongoDB database instance.
#     """
#     return db