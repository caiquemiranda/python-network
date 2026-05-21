from netmiko import ConnectHandler

R1 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.101',
   'username': 'miranda',
   'password': 'cisco',
   }
R2 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.102',
   'username': 'miranda',
   'password': 'cisco',
   }
R3 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.103',
   'username': 'miranda',
   'password': 'cisco',
   }

for routers in (R1, R2, R3):
   connect = ConnectHandler(**routers)
   print(connect.find_prompt())
   connect.disconnect()

print('Script finalizado')