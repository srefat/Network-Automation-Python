from netmiko import ConnectHandler

mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.111.200',
    'username': 'admin',
    'password': '',
}

print("Connecting to MikroTik...")
conn = ConnectHandler(**mikrotik)

print("Setting hostname...")
conn.send_command_timing('/system identity set name=GNS3-Router')

print("Setting DNS...")
conn.send_command_timing('/ip dns set servers=8.8.8.8,8.8.4.4')

print("\n--- Hostname ---")
print(conn.send_command('/system identity print'))

print("\n--- DNS ---")
print(conn.send_command('/ip dns print'))

conn.disconnect()
print("\nDone! Router configured successfully!")