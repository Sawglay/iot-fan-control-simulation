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

    def gateway_validate(command: dict[str, Any]) -> tuple[bool, str]:
        """Check whether the gateway should forward this command."""
        # TODO 2: reject unknown device identifiers.
        if command['deviceId'] not in DEVICES:
            return False, f"Unknown DeviceID : {command['deviceId']}"
        
        # TODO 3: reject commands that are not "setPower".
        if command["command"] != "setPower":
            return False, f"Invalid Command : {command['command']}"

        # TODO 4: reject values that are not "on" or "off".
        if command["value"] == "on":
            return True, 'Valid Command'
        elif command['value'] == "off":
            return True, 'Valid Command'
        else:
            return False, "Invalid Values"
        
        # raise NotImplementedError("TODO 2-4: validate deviceId, command, and value.")

    def device_apply_command(command: dict[str, Any]) -> dict[str, Any]:
        """Apply an accepted command to the simulated device state."""
        device_id = command["deviceId"]
        value = command["value"]

    # TODO 5: update DEVICES[device_id]["power"] with the requested value.
        DEVICES[device_id]["power"] = value,

    # raise NotImplementedError("TODO 5: apply the accepted command to the device.")

        return {
            "deviceId": device_id,
            "reported": deepcopy(DEVICES[device_id]),
            "status": "accepted",
            "timestamp": utc_timestamp(),
        }
    def application_display_result(result: dict[str, Any] | None) -> None:
        """Display reported state without pretending that a request always worked."""
        if result is None:
            trace("application", "No result yet: command outcome is unconfirmed.")
            return

        trace(
            "application",
            f"Reported power for {result['deviceId']}: {result['reported']['power']}",
        )
    def run_exchange(device_id: str, value: str, *, simulate_missing_result: bool = False) -> None:
        """Run one application -> gateway -> device -> application exchange."""
        trace("initial device states", deepcopy(DEVICES))

        command = application_create_command(device_id, value)
        trace("application command", command)

        accepted, reason = gateway_validate(command)
        trace("gateway decision", reason)

        if not accepted:
            trace("device action", "Command rejected before reaching the device.")
            application_display_result(
                {
                    "deviceId": device_id,
                    "reported": {"power": "unchanged"},
                    "status": "rejected",
                    "reason": reason,
                    "timestamp": utc_timestamp(),
                }
            )
            return

        result = device_apply_command(command)
        trace("device result", result)

        if simulate_missing_result:
            application_display_result(None)
        else:
            application_display_result(result)
