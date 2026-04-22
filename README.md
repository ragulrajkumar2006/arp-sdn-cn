# Secure ARP SDN Controller using Ryu and Mininet

## 👤 Developer Information
- **Name:** Ragul Rajkumar S
- **SRN:** PES2UG24AM128
- **Course:** Microprocessor and Computer Architecture (MPCA) / Computer Networks
- **Institution:** PES University

---

## 📌 Project Overview
This project demonstrates a **Software Defined Networking (SDN)** approach to address resolution. It implements a custom **ARP Proxy** and **Learning Switch** using the **Ryu Controller** framework and **OpenFlow 1.3**.

The primary goal is to reduce network broadcast traffic. Instead of flooding ARP requests to every host, the SDN controller intercepts the request and provides a Unicast ARP reply if the target's MAC address is already known in the controller's internal ARP table.

---

## 🛠 Features
- **Dynamic Learning:** The controller builds a `mac_to_port` table by inspecting incoming packets, allowing it to function as a Layer 2 switch.
- **ARP Proxy Logic:** Intercepts `ARP_REQUEST` packets. If the destination IP is in the controller's cache, it generates an `ARP_REPLY` on behalf of the target host.
- **Flow Rule Management:** Automatically installs OpenFlow rules into the switch (OVS) with a priority of 1 to handle subsequent traffic efficiently in hardware.
- **Custom Topology:** A Mininet-based star topology consisting of 1 Open vSwitch and 4 isolated hosts.

---

## 📂 File Descriptions
| File | Description |
| :--- | :--- |
| `arp_controller.py` | The Ryu application containing the control logic for ARP handling and flow installation. |
| `topology.py` | The Python script that initializes the Mininet environment, links hosts, and connects to the remote controller. |

---
