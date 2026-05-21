import getpass
import telnetlib

HOST = "192.168.0.103"
user = input("Digite o seu usuario: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")


tn.write(b"conf t\n")
tn.write(b"interface gi0/1\n")
tn.write(b"ip add 10.100.203.2 255.255.255.252\n")
tn.write(b"no shutdown\n")

tn.write(b"interface loo 0\n")
tn.write(b"ip add 3.3.3.3 255.255.255.0\n")
tn.write(b"no shutdown\n")

tn.write(b"router ospf 1\n")
tn.write(b"network 10.100.203.0 0.0.0.3 area 0 \n")
tn.write(b"network 3.3.3.0 0.0.0.255 area 0 \n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
