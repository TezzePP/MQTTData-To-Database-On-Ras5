from supabase import create_client

from config import (
    SUPABASE_URL,
    SUPABASE_KEY
)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def insert_measurement(data):

    result = supabase.table(
        "measurements"
    ).insert({

        "temperature": data.get("temperature"),
        "humidity": data.get("humidity"),
        "co2": data.get("co2"),
        "device_id": data.get("device_id")

    }).execute()

    return result