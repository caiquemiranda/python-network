from netmiko import ConnectHandler

R1 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.101',
   'username': 'andre',
   'password': 'cisco',
   }
R2 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.102',
   'username': 'andre',
   'password': 'cisco',
   }
R3 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.103',
   'username': 'andre',
   'password': 'cisco',
   }

with open('config-router-file') as file:
   config_lines = file.read().splitlines()

lista_routers = [R1, R2, R3]

for routers in lista_routers:
   connect = ConnectHandler(**routers)
   configure = connect.send_config_set(config_lines)
   print(configure)
   connect.disconnect()