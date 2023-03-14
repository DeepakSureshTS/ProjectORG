import pymongo 

conn = pymongo.MongoClient('localhost', 27017)
db = conn[ "SCMDb" ]
collection_name = db["newuser"]
collection_shipment = db["shipmentdetails"]
collection_device=db["device_data"]

# bootstrap_servers = ['localhost:9092']
# topicName = 'device_data'