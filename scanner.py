import socket
import threading
import time
import ipaddress


def scan_port(target, port, open_ports, lock):
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

            with lock:
                open_ports.append((port, service))

    finally:
        sock.close()


def main():
    target = input("Enter an IP address: ")

    # Validate the IP address
    try:
        ipaddress.ip_address(target)
    except ValueError:
        print("Invalid IP address.")
        return

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))
    except ValueError:
        print("Please enter valid port numbers.")
        return

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range.")
        return

    print(
        f"\nScanning {target} "
        f"from port {start_port} to {end_port}...\n"
    )

    start_time = time.time()

    open_ports = []
    lock = threading.Lock()
    threads = []

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(
            target=scan_port,
            args=(target, port, open_ports, lock)
        )

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

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