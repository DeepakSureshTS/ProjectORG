import os
import pymongo 
from dotenv import load_dotenv
import urllib.parse

load_dotenv(dotenv_path=".env")

username = urllib.parse.quote_plus(os.getenv("dbUsername"))
password = urllib.parse.quote_plus(os.getenv("dbPassword"))

url = os.getenv("dbUri").format(username, password)

client = pymongo.MongoClient(url)

db =client["SCMXpert"]
collection_name = db["User"]
collection_shipment = db["Shipments"]
collection_device=db["device_data"]
