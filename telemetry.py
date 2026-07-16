import psutil
import random


# ==========================================
# Laptop Telemetry
# ==========================================

class LaptopTelemetry:

    def collect(self):

        return {

            "cpu": psutil.cpu_percent(),

            "memory": psutil.virtual_memory().percent

        }


# ==========================================
# Fake Phone Telemetry
# ==========================================

class FakePhoneTelemetry:

    def __init__(self):

        self.cpu = 25
        self.memory = 42

    def collect(self):

        # Simulate changing load

        self.cpu += random.randint(-5, 5)
        self.memory += random.randint(-2, 2)

        self.cpu = max(5, min(80, self.cpu))
        self.memory = max(20, min(70, self.memory))

        return {

            "cpu": self.cpu,

            "memory": self.memory

        }