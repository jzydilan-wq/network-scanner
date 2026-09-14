import socket
import time
import ipaddress
from concurrent.futures import ThreadPoolExecutor


def scan_port(target, port):
    """
    Check whether a TCP port is open.
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "Unknown"

            return port, service

    finally:
        sock.close()

    return None


def main():
    target = input("Enter an IP address: ")

    # Validate the IP address
    try:
        ipaddress.ip_address(target)
    except ValueError:
        print("Invalid IP address.")
        return

    # Get the port range
    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))
    except ValueError:
        print("Please enter valid port numbers.")
        return

    # Validate the port range
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range.")
        return

    print(
        f"\nScanning {target} "
        f"from port {start_port} to {end_port}...\n"
    )

    start_time = time.time()

    open_ports = []

    # Create a pool of 100 worker threads
    with ThreadPoolExecutor(max_workers=100) as executor:

        results = executor.map(
            lambda port: scan_port(target, port),
            range(start_port, end_port + 1)
        )

        for result in results:
            if result is not None:
                open_ports.append(result)

    scan_time = time.time() - start_time
    ports_scanned = end_port - start_port + 1

    print("\nScan complete!")
    print("--------------------------------")
    print(f"Ports scanned: {ports_scanned}")
    print(f"Open ports:    {len(open_ports)}")
    print(f"Scan time:     {scan_time:.2f} seconds")

    if open_ports:
        print("\nOpen ports:")

        for port, service in sorted(open_ports):
            print(f"  → Port {port} ({service})")
    else:
        print("\nNo open ports found.")


if __name__ == "__main__":
    main()