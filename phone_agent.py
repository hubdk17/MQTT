from agents.base_agent import BaseAgent
from agents.telemetry import FakePhoneTelemetry


agent = BaseAgent(

    node_name="PHONE_01",

    capabilities=[

        "image",

        "ocr"

    ],

    telemetry_provider=FakePhoneTelemetry()

)

agent.connect()