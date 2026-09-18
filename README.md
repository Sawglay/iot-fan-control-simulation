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

