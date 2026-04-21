# Packet Logger using SDN Controller

## Problem Statement
This project implements a packet logger using Software Defined Networking (SDN). The controller captures packets, identifies protocol types (ICMP, TCP, UDP), and logs packet information such as source and destination IP addresses.

## Tools Used
- Mininet
- POX Controller
- OpenFlow

## Setup Instructions

1. Install Mininet:
   sudo apt install mininet

2. Clone POX:
   git clone https://github.com/noxrepo/pox
   cd pox

3. Add packet_logger.py inside pox folder

4. Run Controller:
   ./pox.py packet_logger

5. Run Mininet:
   sudo mn --topo single,2 --controller remote

## Functionality

- Captures packets using PacketIn events
- Identifies protocol type (ICMP, TCP, UDP)
- Logs packet details (source IP, destination IP, protocol)
- Forwards packets using OpenFlow packet_out (flooding)

## Test Scenarios

### 1. ICMP Test
Command:
pingall

Output:
Controller logs ICMP packets

### 2. TCP Test
Commands:
h2 iperf -s  
h1 iperf -c 10.0.0.2

Output:
Controller logs TCP packets

### 3. UDP Test
Commands:
h2 iperf -s -u  
h1 iperf -c 10.0.0.2 -u

Output:
Controller logs UDP packets
## Output

- Packet logs displayed in controller terminal
- ICMP, UDP and TCP packets successfully detected

## Screenshots

Screenshots of execution are provided in the repository. 

## Conclusion

This project demonstrates SDN controller functionality including packet monitoring, protocol detection, and network behavior observation using Mininet and POX.
