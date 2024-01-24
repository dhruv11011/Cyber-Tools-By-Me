import scapy.all as scapy
import os

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"IP Source: {ip_src} | IP Destination: {ip_dst}")

        if packet.haslayer(scapy.TCP):
            tcp_src = packet[scapy.TCP].sport
            tcp_dst = packet[scapy.TCP].dport
            print(f"TCP Source Port: {tcp_src} | TCP Destination Port: {tcp_dst}")

            if packet.haslayer(scapy.Raw):
                data = packet[scapy.Raw].load
                if data:
                    print(f"Data: {data.decode('utf-8')}")
            else:
                print("No Raw layer found")

def start_sniffer(interface):
    while True:
        try:
            scapy.sniff(iface=interface, store=False, prn=packet_callback)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    os.system('cls')
    print("\t\tThis is Packet Sniffer Tools Made By Dhruv Bhatt")
    target_interface = input("Enter the network interface to sniff (e.g., Ethernet, Wi-Fi): ")
    start_sniffer(target_interface)
