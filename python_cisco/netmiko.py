from netmiko import ConnectHandler

R1 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.101',
   'username': 'miranda',
   'password': 'cisco',
   }

connect = ConnectHandler(**R1)

output = connect.send_command('show run')
print(output)