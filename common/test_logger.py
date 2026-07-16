import json

from common.device import Device

import common.protocol as protocol

device = Device("PHONE_01")

packet = protocol.register(

    sender="PHONE_01",

    capabilities=[

        "image",

        "ocr"

    ]

)

device.update(packet)

packet = protocol.telemetry(

    sender="PHONE_01",

    cpu=31,

    memory=42,

    battery=87,

    temperature=33.2,

    latency=18

)

device.update(packet)

print(device)

print()

print(device.to_dict())