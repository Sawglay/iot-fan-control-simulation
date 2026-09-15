"""Lesson 02 starter: internet-based IoT device control simulation.

Run:
    python fan_control_lab.py

Complete the TODOs during the lab. The file uses only the Python standard
library so it can run without installing packages.
"""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any


DEVICES: dict[str, dict[str, str]] = {
    "sim-fan-01": {"power": "off"},
    "sim-fan-02": {"power": "off"},
}

VALID_POWER_VALUES = {"on", "off"}


def utc_timestamp() -> str:
    """Return an ISO 8601 timestamp for traceable messages."""
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def trace(stage: str, detail: Any) -> None:
    """Print one compact trace line for the control exchange."""
    print(f"\n[{stage}]")
    print(detail)


def application_create_command(device_id: str, value: str) -> dict[str, Any]:
    """Create the command requested by the user-facing application."""
    # TODO 1: return a structured command dictionary with these fields:
    # deviceId, command, value, requestedBy, timestamp.
    # The command field must be "setPower".
    return {
        "deviceId" : device_id,
        "command" : "setPower",
        "value" : value,
        "requestedBy" : "application",
        "timestamp" : utc_timestamp(),
     }
    # raise NotImplementedError("TODO 1: build the application command dictionary.")