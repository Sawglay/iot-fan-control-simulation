
# IoT Fan Control Simulation

A Python lab that demonstrates how an application sends a power command through a gateway to a simulated IoT fan and receives its reported state.

This project models an internet-based IoT control workflow locally. It does not connect to the internet or control physical hardware.

## Features

- Two simulated fans, initially switched off.
- Structured commands with device identifiers and UTC timestamps.
- Gateway validation of device IDs, command types, and power values.
- Device state updates and reported results.
- Console traces for each stage of the exchange.
- A missing-result scenario that demonstrates why sending a command does not guarantee confirmation.
  
## Requirements

- Python 3.10 or newer recommended.
- No third-party packages or hardware required.

The script uses only Python's standard library: `copy`, `datetime`, and `typing`.

## Before Running the Supplied Code

The pasted lab code needs two corrections before it behaves as described below:

1. Move `gateway_validate`, `device_apply_command`, `application_display_result`, `run_exchange`, and `main` to the top level. Also move the `if __name__ == "__main__":` block to the top level. They are currently nested inside `application_create_command`, after its `return`, so the program does not reach them.
2. Remove the trailing comma from the device state assignment:

   ```python
   DEVICES[device_id]["power"] = value
   ```

   Using `value,` creates a one-item tuple such as `('on',)` instead of storing the string `"on"`.

## Run the Lab

Save the Python code as `fan_control_lab.py`, apply the corrections above, and open a terminal in the same directory.

```bash
python fan_control_lab.py
```

If your system uses `python3`:

## How It Works

1. **Application:** Creates a command containing the target device and requested power value.
2. **Gateway:** Checks that the device exists, the command is `setPower`, and the value is `on` or `off`.
3. **Device:** Applies an accepted command to its in-memory state and creates a result.
4. **Application:** Displays the reported power state, or indicates that the outcome is unconfirmed if no result is received.

Rejected commands stop at the gateway and do not change device state.

```bash
python3 fan_control_lab.py
```

The script runs four predefined scenarios automatically; it does not prompt for user input.

### Example Command

```python
{
    "deviceId": "sim-fan-01",
    "command": "setPower",
    "value": "on",
    "requestedBy": "application",
    "timestamp": "2026-09-18T12:00:00+00:00"
}
```

The timestamp above is illustrative; the program generates the current UTC timestamp for each message.

### Simulated Devices

| Device ID | Initial power |
| --- | --- |
| `sim-fan-01` | `off` |
| `sim-fan-02` | `off` |

## Lab Scenarios

The expected behavior below assumes the two code corrections have been applied. Scenarios run in order and share device state.

| Scenario | Request | Gateway decision | Outcome |
| --- | --- | --- | --- |
| A: Valid command | Turn `sim-fan-01` `on` | Accepted | Fan turns on; application displays `on`. |
| B: Invalid value | Set `sim-fan-01` to `start` | Rejected | Fan remains on. |
| C: Unknown device | Turn `sim-fan-99` `off` | Rejected | No device state changes. |
| D: Missing result | Turn `sim-fan-01` `off` | Accepted | Fan turns off, but application reports an unconfirmed outcome. |

In Scenario D, the simulation prints the device result in its trace but deliberately withholds that result from the application display function.

Expected final device states:

```python
{
    "sim-fan-01": {"power": "off"},
    "sim-fan-02": {"power": "off"}
}
```

## Main Functions

| Function | Purpose |
| --- | --- |
| `utc_timestamp()` | Generates an ISO 8601 UTC timestamp. |
| `trace()` | Prints a labeled stage and its details. |
| `application_create_command()` | Builds the application's command dictionary. |
| `gateway_validate()` | Returns an acceptance flag and a reason. |
| `device_apply_command()` | Updates device power and returns a snapshot of its state. |
| `application_display_result()` | Displays reported power or an unconfirmed-outcome message. |
| `run_exchange()` | Coordinates one complete control exchange. |
| `main()` | Runs the four demonstration scenarios. |

## Lab TODOs

| TODO | Task |
| --- | --- |
| 1 | Build a command with `deviceId`, `command`, `value`, `requestedBy`, and `timestamp`. |
| 2 | Reject unknown device identifiers. |
| 3 | Reject command types other than `setPower`. |
| 4 | Reject power values other than `on` and `off`. |
| 5 | Update the target device's power state. |

The supplied code includes implementations for these TODOs, with the corrections noted above still required.

## Learning Outcomes

- Understand the roles of an application, gateway, and device in IoT control.
- Build and validate structured command messages using Python dictionaries.
- Distinguish requested state from reported state.
- Understand that a missing response does not necessarily mean a command failed.
- Use timestamps and console traces to follow an exchange.

## Limitations

- State is stored in memory and resets when the script restarts.
- No real network protocols, authentication, or physical devices are implemented.
- Validation assumes the required dictionary keys are present.
- The invalid-command-type check exists, but the four built-in scenarios do not exercise it.
- For rejected requests, `"unchanged"` is a display marker, not a reading of the device's actual power state.
