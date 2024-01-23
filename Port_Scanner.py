import socket
import os

def scan_target(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()

if __name__ == "__main__":
    os.system('cls')
    print("\t\tThis is Port Scanner Tools Made By Dhruv Bhatt")
    target_ip = input("Enter target IP address: ")
    target_ports = [int(port) for port in input("Enter target ports (comma-separated): ").split(",")]

    scan_target(target_ip, target_ports)
