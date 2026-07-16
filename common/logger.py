"""
=========================================================
Marketplace Runtime v2
Logger Module
=========================================================
"""

from datetime import datetime


# -------------------------------------------------------
# Internal Formatter
# -------------------------------------------------------

def _timestamp():

    return datetime.now().strftime("%H:%M:%S")


# -------------------------------------------------------
# Generic Logger
# -------------------------------------------------------

def log(component, message):

    print(
        f"[{_timestamp()}] "
        f"[{component}] "
        f"{message}"
    )


# -------------------------------------------------------
# Success
# -------------------------------------------------------

def success(component, message):

    print(
        f"[{_timestamp()}] "
        f"[{component}] "
        f"[SUCCESS] "
        f"{message}"
    )


# -------------------------------------------------------
# Warning
# -------------------------------------------------------

def warning(component, message):

    print(
        f"[{_timestamp()}] "
        f"[{component}] "
        f"[WARNING] "
        f"{message}"
    )


# -------------------------------------------------------
# Error
# -------------------------------------------------------

def error(component, message):

    print(
        f"[{_timestamp()}] "
        f"[{component}] "
        f"[ERROR] "
        f"{message}"
    )


# -------------------------------------------------------
# Divider
# -------------------------------------------------------

def divider(title=""):

    print()

    print("=" * 60)

    if title != "":
        print(title)

    print("=" * 60)