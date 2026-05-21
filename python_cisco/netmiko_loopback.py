from netmiko import ConnectHandler

R1 = {
   'device_type': 'cisco_ios',
   'host': '192.168.0.101',
   'username': 'miranda',
   'password': 'cisco',
   }

net_connect = ConnectHandler(**R1)

nova_loopback = ['interface loopback 13']

configurar = net_connect.send_config_set(nova_loopback)
verificar = net_connect.send_command("show ip int brief")

print(configurar)
print(verificar)
