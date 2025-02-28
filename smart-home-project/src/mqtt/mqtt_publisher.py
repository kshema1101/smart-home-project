from pymongo import MongoClient
from datetime import datetime
import paho.mqtt.client as mqtt
import time

# MongoDB Atlas connection string
#MONGO_URI = "mongodb+srv://kshema:Maria@97@cluster0.agsc5.mongodb.net/smarthome?retryWrites=true&w=majority"
MONGO_URI = "mongodb+srv://kshema:Maria%4097@cluster0.agsc5.mongodb.net/smarthome?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.smarthome  # Database name
collection = db.sensor_data  # Collection name

MQTT_BROKER = "localhost"  # Change if needed
MQTT_TOPIC = "home/sensor"
DATA_FILE = "/Users/nikhil/smart-home-project/smart-home-project/esp32/sensor_simulation/sensor_data.txt"

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, 1883, 60)

def read_and_publish():
    last_data = ""  # Store the last data read from the file
    while True:
        try:
            # Open the file and read the content
            with open(DATA_FILE, "r") as file:
                data = file.read().strip()

            # Only publish and save if the data has changed
            if data != last_data:
                last_data = data
                # Parse the temperature and humidity from the file
                temperature, humidity = data.split(",")
                payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'

                # Publish the data to MQTT
                mqtt_client.publish(MQTT_TOPIC, payload)
                print(f"Published: {payload}")

                # Save the data to MongoDB
                sensor_data = {
                    "temperature": float(temperature),
                    "humidity": float(humidity),
                    "timestamp": datetime.utcnow()  # Store the current timestamp
                }
                collection.insert_one(sensor_data)  # Insert data into MongoDB
                print("Data saved to MongoDB")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(5)  # Wait for 5 seconds before checking the file again

if __name__ == "__main__":
    read_and_publish()
