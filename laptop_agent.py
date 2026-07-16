import socket

from agents.base_agent import BaseAgent
from agents.telemetry import LaptopTelemetry

NODE_NAME = socket.gethostname()

agent = BaseAgent(

    node_name=NODE_NAME,

    capabilities=[

        "prime",

        "matrix",

        "image"

    ],

    telemetry_provider=LaptopTelemetry()

)

agent.connect()