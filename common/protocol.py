"""
=========================================================
Marketplace Runtime v2
Protocol Definition
=========================================================
"""

import uuid
from datetime import datetime


# =========================================================
# Base Message
# =========================================================

def create_message(sender, message_type, payload):

    return {

        "message_id": str(uuid.uuid4()),

        "timestamp": datetime.utcnow().isoformat(),

        "sender": sender,

        "type": message_type,

        "payload": payload

    }


# =========================================================
# Registration
# =========================================================

def register(sender, capabilities):

    payload = {

        "capabilities": capabilities

    }

    return create_message(

        sender,

        "register",

        payload

    )


# =========================================================
# Telemetry
# =========================================================

def telemetry(

        sender,

        cpu,

        memory,

        battery=None,

        temperature=None,

        latency=None,

        status="ONLINE"

):

    payload = {

        "cpu": cpu,

        "memory": memory,

        "battery": battery,

        "temperature": temperature,

        "latency": latency,

        "status": status

    }

    return create_message(

        sender,

        "telemetry",

        payload

    )


# =========================================================
# Task
# =========================================================

def task(

        sender,

        task_id,

        operation,

        payload_data

):

    payload = {

        "task_id": task_id,

        "operation": operation,

        "data": payload_data

    }

    return create_message(

        sender,

        "task",

        payload

    )


# =========================================================
# Bid
# =========================================================

def bid(

        sender,

        task_id,

        price

):

    payload = {

        "task_id": task_id,

        "price": price

    }

    return create_message(

        sender,

        "bid",

        payload

    )


# =========================================================
# Winner
# =========================================================

def winner(

        sender,

        task_id,

        winner_name

):

    payload = {

        "task_id": task_id,

        "winner": winner_name

    }

    return create_message(

        sender,

        "winner",

        payload

    )


# =========================================================
# Result
# =========================================================

def result(

        sender,

        task_id,

        execution_time,

        result_data,

        status="DONE"

):

    payload = {

        "task_id": task_id,

        "execution_time": execution_time,

        "status": status,

        "result": result_data

    }

    return create_message(

        sender,

        "result",

        payload

    )