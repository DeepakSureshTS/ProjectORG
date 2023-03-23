import json
from pathlib import Path
from mongoengine import connect
from kafka import KafkaConsumer
from pydantic import BaseModel
import sys
import models
import os
from dotenv import load_dotenv
import urllib.parse


load_dotenv()

base_dir = Path(__file__).resolve().parent
username = urllib.parse.quote_plus('deepak')
password = urllib.parse.quote_plus("demo@123")

url = "mongodb+srv://{}:{}@scmxpert.73z8rrw.mongodb.net/?retryWrites=true&w=majority".format(username, password)

connect(db="SCMXpert", host= url)
bootstrap_servers = 'backend-kafka-1:9092'
topicName = 'device_data'

class DeviceData(BaseModel):
        Battery_Level: int
        Device_Id: int
        First_Sensor_temperature: int
        Route_From: str
        Route_To: str

try:
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')
    for data in consumer:
        data = json.loads(data.value)
        Transport_Data = models.DeviceData(
            Battery_Level = data['Battery_Level'],
            Device_Id = data['Device_Id'],
            First_Sensor_temperature = data['First_Sensor_temperature'],
            Route_From = data['Route_From'],
            Route_To = data['Route_To']                        
        )
        
        Transport_Data.save() 
        print(Transport_Data)
except KeyboardInterrupt:
    sys.exit()