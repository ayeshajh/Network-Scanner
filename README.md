# NetProbe – Python ARP Network Scanner

## Overview

**NetProbe** is a lightweight Python-based ARP network scanner that discovers active devices on a local network by sending ARP requests and collecting responses. It supports scanning both individual IP addresses and entire subnets using CIDR notation.

The project is built using the **Scapy** library and is intended for educational purposes, network administration, and authorized security assessments.

---

## Features

* Scan a single IP address.
* Scan an entire subnet using CIDR notation (e.g., `192.168.1.0/24`).
* Discover active hosts on the local network.
* Display IP and corresponding MAC addresses.
* Input validation for IP addresses and subnet formats.
* Simple command-line interface using `argparse`.
* Basic exception handling for improved reliability.

---

## Technologies Used

* Python 3
* Scapy
* argparse
* ipaddress
* Regular Expressions (re)

---

## Requirements

* Python 3.8 or later
* Root/Administrator privileges (required by Scapy)
* Scapy library

Install Scapy:

```bash
pip install scapy
```

---

## Project Structure

```text
NetProbe/
│
├── scanner.py          # Main scanner script
├── _imports_.py        # Banner module (optional)
├── README.md
└── requirements.txt    # Optional
```

---

## Usage

### Scan a Single Host

```bash
sudo python3 scanner.py -ip 192.168.1.10
```

### Scan a Subnet

```bash
sudo python3 scanner.py -ip 192.168.1.0/24
```

---

## Example Output

```text
==== NetProbe ====

Discovered Devices
------------------
IP: 192.168.1.1      MAC: 48:5d:36:xx:xx:xx
IP: 192.168.1.5      MAC: 70:4d:7b:xx:xx:xx
IP: 192.168.1.12     MAC: 08:00:27:xx:xx:xx
```

---

## How It Works

1. Accepts an IP address or subnet from the command line.
2. Validates the input format.
3. Constructs an ARP request packet.
4. Broadcasts the packet over the local network.
5. Collects ARP replies from active devices.
6. Displays the discovered IP and MAC addresses.

---

## Future Improvements

* Export scan results to CSV or JSON.
* Add multithreaded scanning for improved performance.
* Display vendor information from MAC addresses.
* Implement hostname resolution.
* Add colored terminal output.
* Support custom scan timeout values.
* Build a graphical user interface (GUI).

---

## Disclaimer

This project is intended **only for educational purposes and authorized network administration**. Always obtain permission before scanning any network that you do not own or manage. Unauthorized network scanning may violate organizational policies or applicable laws.

---

## Author

**Ayesha Hussain**

GitHub: *Add your GitHub profile link here*
