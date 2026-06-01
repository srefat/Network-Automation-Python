# Network Automation with Python and MikroTik

## What This Project Does
Python automation scripts that connect to a MikroTik router via SSH and automatically collect network data, backup configurations, and configure router settings — eliminating manual CLI work.

## Problem It Solves
Network engineers manually SSH into devices one by one to check interfaces, IP addresses, and router information. These scripts automate the entire process in seconds.

## Technologies Used
- Python 3.14
- Netmiko library
- MikroTik CHR 7.23 (RouterOS)
- GNS3 with VMware Workstation Pro
- SSH protocol

## How It Works
1. Script SSHs into MikroTik router automatically
2. Pulls IP address table
3. Pulls interface status
4. Pulls router identity
5. Saves everything to a backup file with date and time

## Network Topology
![Network Topology](GNS.png)

## Script Output
![Script Output](out.png)

## Results
- Connected to MikroTik router running in GNS3
- Extracted live network data automatically
- Generated automated backup report
- Configured router hostname and DNS automatically

## Files
- `mikrotik_test.py` — Connects and reads router info
- `mikrotik_backup.py` — Auto backup router configuration
- `mikrotik_configure.py` — Auto configure router settings
- `backup_2026-06-01.txt` — Auto generated backup report

## How To Run
pip install netmiko
python mikrotik_test.py
python mikrotik_backup.py
python mikrotik_configure.py
