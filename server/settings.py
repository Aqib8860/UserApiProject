from pymongo import MongoClient
from datetime import datetime

def clientOpen():
    return MongoClient(f"mongodb+srv://aiworld:i6TO1DZbtBzckOnx@mydb.xci1l.mongodb.net/mydb?retryWrites=true&w=majority")

