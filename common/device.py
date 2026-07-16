"""
=========================================================
Marketplace Runtime v2
Device Model
=========================================================
"""

import time


class Device:

    def __init__(self, node_name):

        # -----------------------------------------
        # Identity
        # -----------------------------------------

        self.node_name = node_name

        # -----------------------------------------
        # Device Information
        # -----------------------------------------

        self.capabilities = []

        # -----------------------------------------
        # Live Telemetry
        # -----------------------------------------

        self.cpu = None
        self.memory = None
        self.battery = None
        self.temperature = None
        self.latency = None

        # -----------------------------------------
        # Marketplace State
        # -----------------------------------------

        self.status = "OFFLINE"

        self.current_task = None

        self.last_bid = None

        self.last_reward = None

        # -----------------------------------------
        # Communication
        # -----------------------------------------

        self.last_seen = 0

        self.last_message_id = None

        self.last_timestamp = None

        self.total_messages = 0

    # =====================================================
    # Registration Packet
    # =====================================================

    def update_registration(self, packet):

        self.capabilities = packet["payload"]["capabilities"]

        self.last_seen = time.time()

        self.status = "ONLINE"

        self.last_message_id = packet["message_id"]

        self.last_timestamp = packet["timestamp"]

        self.total_messages += 1

    # =====================================================
    # Telemetry Packet
    # =====================================================

    def update_telemetry(self, packet):

        payload = packet["payload"]

        self.cpu = payload.get("cpu")

        self.memory = payload.get("memory")

        self.battery = payload.get("battery")

        self.temperature = payload.get("temperature")

        self.latency = payload.get("latency")

        self.status = payload.get("status", "ONLINE")

        self.last_seen = time.time()

        self.last_message_id = packet["message_id"]

        self.last_timestamp = packet["timestamp"]

        self.total_messages += 1

    # =====================================================
    # Generic Update
    # =====================================================

    def update(self, packet):

        packet_type = packet["type"]

        if packet_type == "register":

            self.update_registration(packet)

        elif packet_type == "telemetry":

            self.update_telemetry(packet)

    # =====================================================
    # Heartbeat Check
    # =====================================================

    def check_alive(self, timeout=5):

        if time.time() - self.last_seen > timeout:

            self.status = "OFFLINE"

        else:

            self.status = "ONLINE"

    # =====================================================
    # Dictionary (Dashboard Friendly)
    # =====================================================

    def to_dict(self):

        return {

            "Node": self.node_name,

            "CPU": self.cpu,

            "Memory": self.memory,

            "Battery": self.battery,

            "Temperature": self.temperature,

            "Latency": self.latency,

            "Status": self.status,

            "Capabilities": self.capabilities,

            "Current Task": self.current_task,

            "Last Bid": self.last_bid,

            "Reward": self.last_reward,

            "Messages": self.total_messages

        }

    # =====================================================
    # Pretty Print
    # =====================================================

    def __str__(self):

        return (
            f"{self.node_name} | "
            f"CPU={self.cpu} | "
            f"RAM={self.memory} | "
            f"Battery={self.battery} | "
            f"Temp={self.temperature} | "
            f"Status={self.status}"
        )