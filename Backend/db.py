import pymongo 
from dotenv import dotenv_values
import urllib.parse

username = urllib.parse.quote_plus('deepak')
password = urllib.parse.quote_plus("demo@123")

url = "mongodb+srv://{}:{}@scmxpert.73z8rrw.mongodb.net/?retryWrites=true&w=majority".format(username, password)

client = pymongo.MongoClient(url)

db =client["SCMXpert"]
collection_name = db["newuser"]
collection_shipment = db["shipmentdetails"]
collection_device=db["device_data"]
