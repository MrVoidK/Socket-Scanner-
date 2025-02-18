#!/bin/python3

import sys
import socket
import threading
import itertools
import time
from datetime import datetime

# Define our target
if len(sys.argv) == 2:  # Control the number of arguments
    target = socket.gethostbyname(sys.argv[1])  # Convert hostname to IP
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Add a banner
_dateTime = str(datetime.now())
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + _dateTime)
print("-" * 50)

# Loading animation flag
loading = True

# Function for loading animation
def loading_animation():
    for symbol in itertools.cycle(["|", "/", "-", "\\"]):
        if not loading:
            break
        sys.stdout.write(f"\rScanning ports... {symbol}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\rScanning complete!        \n")  # Clear the line

# Start the animation in a separate thread
animation_thread = threading.Thread(target=loading_animation)
animation_thread.start()

try:
    socket.setdefaulttimeout(1)  # Set timeout for connections
    open_ports = []

    for port in range(50, 85):  # Scan ports between 50-85
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        result = s.connect_ex((target, port))  # Try to connect to the target's port
        if result == 0:  # If port is open, result is '0'
            open_ports.append(port)
        s.close()  # Close the socket to free resources

    # Stop the loading animation
    loading = False
    animation_thread.join()

    # Print and write open ports to file
    with open("scanner_data.txt", "a") as file:
        file.write(f"\nScan started at {_dateTime} for target: {target}\n")

        if open_ports:
            print("Open ports:")
            for port in open_ports:
                print(f"- Port {port} is open")
                file.write(f"- Port {port} is open\n")  # Writing inside the 'with' block
        else:
            print("No open ports found.")
            file.write("No open ports found.\n")  #  Writing inside the 'with' block

except KeyboardInterrupt:  # Press Ctrl + C
    loading = False
    animation_thread.join()
    print("\nExiting program...")
    sys.exit()

except socket.gaierror:  # When hostname is not found
    loading = False
    animation_thread.join()
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    loading = False
    animation_thread.join()
    print("Could not connect to server.")
    sys.exit()
