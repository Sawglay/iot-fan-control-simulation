
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
