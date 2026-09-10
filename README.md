# Python Network Scanner

A simple TCP port scanner built with Python. This project was created to learn the basics of network scanning, TCP connections, sockets, and multithreading.

## Features

* Scan a custom range of TCP ports
* Detect open ports
* Identify common services
* Use multithreading to speed up scanning
* Display scan duration
* Validate port input

## Technologies

* Python 3
* Socket programming
* TCP/IP
* Multithreading

## How It Works

The scanner attempts to connect to each port on a target IP address.

If the connection succeeds, the port is considered **open**. If the connection fails, the port is considered **closed**.

The scanner uses multiple threads so that several ports can be checked at the same time.

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python3 scanner.py
```

The program will ask you for:

```text
Enter an IP address: 127.0.0.1
Enter starting port: 1
Enter ending port: 100
```

### Example Output

```text
Scanning 127.0.0.1 from port 1 to 100...

Scan complete!
--------------------------------
Ports scanned: 100
Open ports:    0
Scan time:     0.16 seconds

No open ports found.
```

## What I Learned

This project helped me learn about:

* IP addresses
* TCP ports
* TCP connections
* Python sockets
* Multithreading
* Thread synchronization
* Input validation
* Basic network reconnaissance

## Disclaimer

This project is for educational purposes and authorized security testing only.

Only scan systems that you own or have explicit permission to test.
