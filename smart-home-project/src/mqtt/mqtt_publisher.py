import paho.mqtt.client as mqtt
import time

MQTT_BROKER = "localhost"  # Change if needed
MQTT_TOPIC = "home/sensor"
DATA_FILE = "/Users/nikhil/smart-home-project/smart-home-project/esp32/sensor_simulation/sensor_data.txt"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

def read_and_publish():
    last_data = ""  # Store the last data read from the file
    while True:
        try:
            # Open the file and read the content
            with open(DATA_FILE, "r") as file:
                data = file.read().strip()

            # Only publish if the data has changed
            if data != last_data:
                last_data = data
                # Parse the temperature and humidity from the file
                temperature, humidity = data.split(",")
                payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'
                
                # Publish the data to MQTT
                client.publish(MQTT_TOPIC, payload)
                print(f"Published: {payload}")

        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(5)  # Wait for 5 seconds before checking the file again

if __name__ == "__main__":
    read_and_publish()
