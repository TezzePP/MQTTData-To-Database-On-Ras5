import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "app"))

import mqtt_client

mqtt_client.start_mqtt()