import pygatt

# Define the UUID of the service and characteristic
SERVICE_UUID = "01234567-0123-4567-89ab-0123456789ab"
CHARACTERISTIC_UUID = "01234567-0123-4567-89ab-0123456789ef"

def handle_notification(handle, value):
    print("Received data:", value.decode())

def connect_and_read_characteristic():
    # Create a BLE adapter
    port = "COM7"  # Windows
    adapter = pygatt.BGAPIBackend(serial_port=port)
    # adapter = pygatt.BGAPIBackend()

    try:
        adapter.start()
        print("Scanning for devices...")
        device = adapter.connect("E89F6D09062C")
        print("Connected to device.")

        # Enable notifications for the characteristic
        device.subscribe(CHARACTERISTIC_UUID, callback=handle_notification)

        # Keep the script running
        input("Press Enter to disconnect...\n")

    finally:
        adapter.stop()

if __name__ == "__main__":
    connect_and_read_characteristic()
