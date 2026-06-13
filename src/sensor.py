import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = "mosquitto"
PORT = 1883
TOPIC = "iot/sensors/env"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

while True:
    payload = {
        "sensor_id": f"sensor_{random.randint(1, 3)}",
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 80.0), 2),
        "air_quality": round(random.uniform(50.0, 150.0), 2)
    }
    client.publish(TOPIC, json.dumps(payload))
    print(f"Publicado: {payload}")
    time.sleep(5) # Publica a cada 5 segundos