import pymongo 

conn = pymongo.MongoClient('localhost', 27017)
db = conn[ "SCMDb" ]
collection_name = db["newuser"]
