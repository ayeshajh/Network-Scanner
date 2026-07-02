#!/usr/bin/env python3

import argparse
import ipaddress
from time import sleep
from scapy.all import ARP, Ether, srp

# Optional banner function if _imports_ is not available
try:
    from _imports_ import banner
except ImportError:
    def banner():
        print("==== Python ARP Network Scanner ====\n")

def scan_network(ip_target):
    try:
        # Build ARP + Ethernet packets
        arp = ARP(pdst=ip_target)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        # Send the packet and capture response
        answered, _ = srp(packet, timeout=3, verbose=0)

        # Show discovered clients
        if answered:
            print("Discovered Devices:\n-------------------")
            for sent, received in answered:
                print(f"IP: {received.psrc}\tMAC: {received.hwsrc}")
        else:
            print("No devices found or no response from the network.")

    except Exception as e:
        print(f"Error occurred during scanning: {e}")

def validate_ip(ip_input):
    try:
        # Accept both host and subnet input
        ipaddress.ip_network(ip_input, strict=False)
        return True
    except ValueError:
        return False

def main():
    parser = argparse.ArgumentParser(description="Python ARP Scanner")
    parser.add_argument("-ip", type=str, required=True, help="Target IP or Subnet (e.g. 192.168.1.1 or 192.168.1.0/24)")
    args = parser.parse_args()

    banner()

    if not validate_ip(args.ip):
        print("Invalid IP format. Use 192.168.1.1 for host or 192.168.1.0/24 for subnet.")
        sleep(3)
        exit()

    scan_network(args.ip)

if __name__ == "__main__":
    main()
