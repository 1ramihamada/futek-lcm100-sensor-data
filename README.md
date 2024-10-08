# FUTEK LCM100 Sensor Data Reader

This repository contains Python code for reading force sensor data from a FUTEK LCM100 sensor using the USB225 Pro Elite interface. The code establishes a serial connection with the sensor and provides a CLI interface for connecting, starting data collection, and disconnecting.

## Features
- Connects to the FUTEK LCM100 sensor through the USB225 interface.
- Reads and parses real-time sensor data.
- Displays sensor readings in a user-friendly format.
- CLI interface for connecting, starting data collection, and disconnecting.

## Requirements
- Python 3.x
- `pyserial` library (install with `pip install pyserial`)

## Setup
1. **Connect the Sensor**: Ensure the FUTEK LCM100 sensor is connected to your computer via the USB225 module. Note the serial port (`/dev/ttyUSB0` is the default).
2. **Install Dependencies**: Make sure `pyserial` is installed:
   ```bash
   pip install pyserial
