from netmiko import ConnectHandler
from datetime import datetime

mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.111.200',
    'username': 'admin',
    'password': '',
}

print("Connecting to MikroTik...")
conn = ConnectHandler(**mikrotik)

now = datetime.now().strftime("%Y-%m-%d_%H-%M")

print("\n--- Router Identity ---")
identity = conn.send_command('/system identity print')
print(identity)

print("\n--- IP Addresses ---")
ip = conn.send_command('/ip address print')
print(ip)

print("\n--- Interfaces ---")
interfaces = conn.send_command('/interface print')
print(interfaces)

filename = f"backup_{now}.txt"
with open(filename, 'w') as f:
    f.write("=== MikroTik Backup ===\n")
    f.write(f"Date: {now}\n\n")
    f.write("--- Identity ---\n")
    f.write(identity + "\n\n")
    f.write("--- IP Addresses ---\n")
    f.write(ip + "\n\n")
    f.write("--- Interfaces ---\n")
    f.write(interfaces + "\n")

print(f"\nBackup saved to: {filename}")
conn.disconnect()