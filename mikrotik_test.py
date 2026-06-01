from netmiko import ConnectHandler

mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host': '192.168.111.200',
    'username': 'admin',
    'password': '',
}

print("Connecting to MikroTik...")
connection = ConnectHandler(**mikrotik)

output = connection.send_command('/ip address print')
print(output)

connection.disconnect()
print("Done!")