from pymongo import MongoClient
import certifi

uri = "mongodb+srv://<username>:<password>@cluster0.qtef1.mongodb.net/?retryWrites=true&w=majority"
try:
    client = MongoClient(uri, tlsCAFile=certifi.where())
    client.admin.command('ping')
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
