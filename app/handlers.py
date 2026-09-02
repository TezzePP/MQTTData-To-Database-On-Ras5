import json

from database import insert_measurement


def handle_message(payload):
    try:
        data = json.loads(payload)

        print(f"Received data: {data}")

        insert_measurement(data)

        print("Inserted into Supabase")

    except Exception as e:
        print(f"Handler error: {e}")