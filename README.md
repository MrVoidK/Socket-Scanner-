# Socket Scanner

## Description

This Python program is a simple socket scanner designed to scan open ports on a given target IP address. The program scans ports in the range of 50 to 85 and prints the open ports to the console. Additionally, the results are logged to a file (`scanner_data.txt`).

The program takes the target IP address as a command-line argument, scans each port, and checks whether a connection can be established. If the port is open, it is reported as open. A loading animation is displayed during the scanning process to provide feedback to the user. In case of an error (e.g., inability to resolve the hostname), appropriate error messages are shown.

## Features
- Uses Python's `socket` module to perform port scanning.
- Displays a loading animation while scanning ports.
- Saves scan results to a file (`scanner_data.txt`).
- Takes the target IP address as a command-line argument.
- Scans ports between 50 and 85.
  
## Usage

To use this program, run it from the command line with the target IP address as an argument:

```bash
python3 scanner.py <target-ip>
