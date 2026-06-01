# Network Automation with Python and MikroTik

## Project Overview
This project demonstrates network automation using Python and Netmiko to configure and manage MikroTik routers running in GNS3 with VMware.

## Lab Setup
- **GNS3** — Network simulation platform
- **VMware Workstation Pro** — Virtualization platform
- **MikroTik CHR 7.23** — Virtual router
- **Python 3** + **Netmiko** — Automation library

## Network Topology
Your PC → Cloud (VMnet1) → MikroTik-CHR-1 → PC1 (VPCS)
192.168.111.200


## Scripts

### 1. mikrotik_test.py
Connects to MikroTik and reads IP address table.

### 2. mikrotik_backup.py
Backs up router configuration to a text file automatically with date and time.

### 3. mikrotik_configure.py
Automatically configures router hostname and DNS servers.

## How to Run
```bash
pip install netmiko
python mikrotik_test.py
python mikrotik_backup.py
python mikrotik_configure.py
```

## Skills Demonstrated
- Python scripting
- SSH automation with Netmiko
- Network device configuration
- GNS3 lab setup
- VMware virtualization
