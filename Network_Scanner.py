import scapy.all as scapy
import os

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(results_list):
    print("")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])

if __name__ == "__main__":
    os.system('cls')
    print("\t\tThis is Network Scanner Tools Made By Dhruv Bhatt")
    target_ip = input("Enter the target IP range (e.g., 192.168.1.1/24): ")
    scan_result = scan(target_ip)
    print_result(scan_result)
