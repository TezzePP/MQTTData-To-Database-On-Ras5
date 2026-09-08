# MQTT Data to Database on Raspberry Pi

A Python-based IoT project that receives data through **MQTT** and stores it in a database running on a **Raspberry Pi 5**.

The project was created to experiment with MQTT communication, data handling and persistent storage on a small Linux-based device.

## Overview

The application acts as a bridge between MQTT messages and a database.

The basic flow is:

```text
MQTT Device
     │
     ▼
 MQTT Broker
     │
     ▼
Python MQTT Client
     │
     ▼
Message Handler
     │
     ▼
Database
```

The application starts through `run.py`, which loads the application and starts the MQTT client.

## Technologies

* **Python**
* **MQTT**
* **Raspberry Pi 5**
* **Linux**
* **Database**
* **Paho MQTT** / MQTT client library

## Project Structure

```text
MQTTData-To-Database-On-Ras5/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── handlers.py
│   └── mqtt_client.py
│
├── run.py
├── requirements.txt
└── .gitignore
```

### `mqtt_client.py`

Handles the MQTT connection and receiving messages from the broker.

### `handlers.py`

Contains the logic for processing incoming MQTT messages.

### `database.py`

Handles communication with the database and storing received data.

### `config.py`

Contains configuration used by the application.

### `run.py`

The entry point for the application. It loads the application directory and starts the MQTT client.

## Data Flow

When a device publishes a message to an MQTT topic, the application receives the message through the MQTT client.

The message is then passed to the application logic and stored in the database.

```text
Sensor / Device
       │
       │ MQTT
       ▼
MQTT Broker
       │
       │
       ▼
Raspberry Pi 5
       │
       ├── MQTT Client
       │
       ├── Message Handler
       │
       ▼
   Database
```

## Installation

Clone the repository:

```bash
git clone https://github.com/TezzePP/MQTTData-To-Database-On-Ras5.git
cd MQTTData-To-Database-On-Ras5
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Configure the MQTT broker and database connection in the application configuration.

## Running the Application

Start the application with:

```bash
python run.py
```

The application will start the MQTT client and begin processing incoming messages.

## What I Learned

This project gave me practical experience with:

* MQTT communication
* IoT data collection
* Python application structure
* Working with a Raspberry Pi
* Database integration
* Handling incoming data
* Running Python applications on Linux
* Separating MQTT, processing and database logic

## Project Status

This is a learning project focused on experimenting with MQTT-based data collection and storing IoT data on a Raspberry Pi.

The project can be extended with additional sensors, MQTT topics, database functionality and data visualization.
