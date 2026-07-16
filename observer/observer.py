import json

import paho.mqtt.client as mqtt

from common.config import *
from common import mqtt_topics as TOPICS
from common.logger import log

devices = {}


def on_connect(client, userdata, flags, reason_code, properties):

    log("Observer", "Connected")

    client.subscribe("market/#")


def on_message(client, userdata, msg):

    packet = json.loads(msg.payload.decode())

    topic = msg.topic

    if topic == TOPICS.REGISTER:

        node = packet["node"]

        devices[node] = {

            "capabilities": packet["capabilities"],

            "cpu": None,

            "memory": None

        }

        log("Observer", f"{node} Registered")

    elif topic == TOPICS.TELEMETRY:

        node = packet["node"]

        if node not in devices:

            devices[node] = {}

        devices[node]["cpu"] = packet["cpu"]

        devices[node]["memory"] = packet["memory"]

        print_dashboard()


def print_dashboard():

    print("\n")

    print("=" * 50)

    print("CONNECTED DEVICES")

    print("=" * 50)

    for node, info in devices.items():

        print(f"\n{node}")

        print(f"CPU     : {info.get('cpu')}")

        print(f"Memory  : {info.get('memory')}")

        print(f"Capabilities : {info.get('capabilities')}")

    print("\n")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect

client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()