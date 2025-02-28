from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import seaborn as sns
from pydantic import BaseModel
import io
from fastapi.responses import StreamingResponse

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://kshema:Maria%4097@cluster0.agsc5.mongodb.net/smarthome?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.smarthome  # Database name
collection = db.sensor_data  # Collection name

app = FastAPI()

# Pydantic model for the sensor data
class SensorData(BaseModel):
    temperature: float
    humidity: float
    timestamp: datetime

@app.get("/sensor/latest")
def get_latest_sensor_data():
    """Fetch the latest sensor data from MongoDB"""
    latest_data = collection.find().sort("timestamp", -1).limit(1)
    data = list(latest_data)
    
    if data:
        return {"temperature": data[0]["temperature"], "humidity": data[0]["humidity"], "timestamp": data[0]["timestamp"]}
    else:
        return {"message": "No data available"}

@app.post("/sensor")
def insert_sensor_data(sensor_data: SensorData):
    """Insert new sensor data into MongoDB"""
    collection.insert_one(sensor_data.dict())
    return {"message": "Data inserted successfully"}

@app.get("/data/analytics")
def get_data_analytics():
    """Perform basic data analysis and return averages"""
    cursor = collection.find()
    data = list(cursor)
    
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    avg_temp = df['temperature'].mean()
    avg_humidity = df['humidity'].mean()

    return {"average_temperature": avg_temp, "average_humidity": avg_humidity}

@app.get("/data/plot")
def get_data_plot():
    """Generate a plot for temperature and humidity"""
    cursor = collection.find()
    data = list(cursor)

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Plot Temperature over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['temperature'], label='Temperature', color='r')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature over Time')
    plt.xticks(rotation=45)

    # Save plot to a BytesIO buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    
    return StreamingResponse(buf, media_type="image/png")
