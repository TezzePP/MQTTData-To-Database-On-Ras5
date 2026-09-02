import paho.mqtt.client as mqtt

from config import (
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USER,
    MQTT_PASSWORD,
    MQTT_TOPIC
)

from handlers import handle_message


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"Connection failed: {rc}")


def on_message(client, userdata, msg):
    payload = msg.payload.decode()

    print(f"Topic: {msg.topic}")
    print(f"Payload: {payload}")

    handle_message(payload)


def start_mqtt():
    client = mqtt.Client(
        mqtt.CallbackAPIVersion.VERSION1
    )

    client.username_pw_set(
        MQTT_USER,
        MQTT_PASSWORD
    )

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(
        MQTT_BROKER,
        MQTT_PORT,
        60
    )

    print("MQTT bridge started")

    client.loop_forever()