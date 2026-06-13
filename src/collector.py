import json
import paho.mqtt.client as mqtt
import psycopg2

BROKER = "mosquitto"
PORT = 1883
TOPIC = "iot/sensors/env"

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database="iot_data",
        user="iot_user",
        password="iot_password"
    )

def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO sensor_data (sensor_id, temperature, humidity, air_quality) VALUES (%s, %s, %s, %s)",
            (data['sensor_id'], data['temperature'], data['humidity'], data['air_quality'])
        )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Guardado na DB: {data}")
    except Exception as e:
        print(f"Erro ao guardar na DB: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()