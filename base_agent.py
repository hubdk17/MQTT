import json
import threading
import time

import paho.mqtt.client as mqtt

import common.protocol as protocol
import common.mqtt_topics as topics
from common.config import BROKER, PORT


class BaseAgent:

    def __init__(self,
                 node_name,
                 capabilities,
                 telemetry_provider):

        self.node_name = node_name
        self.capabilities = capabilities
        self.telemetry_provider = telemetry_provider

        self.client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2
        )

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    # -----------------------------------
    # MQTT Connection
    # -----------------------------------

    def connect(self):

        self.client.connect(BROKER, PORT)

        threading.Thread(
            target=self.telemetry_loop,
            daemon=True
        ).start()

        self.client.loop_forever()

    # -----------------------------------
    # Registration
    # -----------------------------------

    def send_registration(self):

        packet = protocol.register(
            self.node_name,
            self.capabilities
        )

        self.client.publish(
            topics.REGISTER,
            json.dumps(packet)
        )

        print(f"[{self.node_name}] Registered")

    # -----------------------------------
    # Telemetry
    # -----------------------------------

    def telemetry_loop(self):

        while True:

            state = self.telemetry_provider.collect()

            packet = protocol.telemetry(
                self.node_name,
                state["cpu"],
                state["memory"]
            )

            self.client.publish(
                topics.TELEMETRY,
                json.dumps(packet)
            )

            print(
                f"[{self.node_name}] "
                f"CPU:{state['cpu']:.1f}% "
                f"RAM:{state['memory']:.1f}%"
            )

            time.sleep(2)

    # -----------------------------------
    # MQTT Callbacks
    # -----------------------------------

    def on_connect(
            self,
            client,
            userdata,
            flags,
            reason_code,
            properties):

        print(f"[{self.node_name}] Connected")

        self.client.subscribe(topics.TASKS)

        self.send_registration()

    def on_message(
            self,
            client,
            userdata,
            msg):

        packet = json.loads(msg.payload.decode())

        print()

        print("=" * 40)

        print(f"[{self.node_name}] NEW TASK")

        print(packet)

        print("=" * 40)