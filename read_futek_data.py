import serial
import re

class USB225SerialDevice:
    def __init__(self, port='/dev/ttyUSB0', baudrate=2000000, timeout=0.1):
        self.port = port # connects to port where USB225 is connect
        self.baudrate = baudrate # The baud rate is the speed of data transmission
        self.timeout = timeout # time (in seconds) to wait before givving up on reading from the port
        self.serial_connection = None # This will store the actual connection object to the device
        self.opened_connection = False # A flag indicating whether the device is connected

    def connect(self):
        try:
            self.serial_connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS, 
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=self.timeout, 
                xonxoff=False,
                rtscts=False,
                dsrdtr=False
            )
            self.opened_connection = True
            print(f"Connected to {self.port} at {self.baudrate} bps.")
        except Exception as e:
            print(f"Error connecting to device: {e}")
            self.opened_connection = False

    def disconnect(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            self.opened_connection = False
            print(f"Disconnected from {self.port}.")
        else:
            print("No active connection to close.")

    def read_sensor_data(self):
        if not self.opened_connection:
            print("No connection to the device.")
            return None

        try:
            while True:
                # Read the response from the device
                response = self.serial_connection.readline().decode('utf-8').strip()

                # If the response is empty, skip it
                if not response:
                    continue

                # Debugging: print the raw response to understand what's coming in
                print(f"Raw response from device: '{response}'")

                # Assuming the format is "DataUnit" or "Data, Unit"
                # Adjust the parsing accordingly
                numeric_value = re.sub("[^0-9.-]", "", response)
                if numeric_value:
                    return float(numeric_value)
                else:
                    print("Invalid numeric value in response.")
                    return None

        except Exception as e:
            print(f"Error reading sensor data: {e}")
            return None


    def start(self):
        if not self.opened_connection:
            print("No connection to start data collection.")
            return

        print("Starting data collection... Press Ctrl+C to stop.")
        try:
            while True:
                sensor_reading = self.read_sensor_data()
                if sensor_reading is not None:
                    print(f"Sensor Reading: {sensor_reading:.6f} lbs")
                else:
                    print("Failed to read sensor data.")
        except KeyboardInterrupt:
            print("Data collection stopped by user.")

    def exit(self):
        self.disconnect()
        print("Exiting the program...")

# CLI Interface for USB225SerialDevice
if __name__ == "__main__":
    device = USB225SerialDevice()

    while True:
        command = input("Enter command (connect/start/disconnect/exit): ").strip().lower()
        if command == 'connect':
            device.connect()
        elif command == 'start':
            device.start()
        elif command == 'disconnect':
            device.disconnect()
        elif command == 'exit':
            device.exit()
            break
        else:
            print("Unknown command. Please enter 'connect', 'start', 'disconnect', or 'exit'.")
