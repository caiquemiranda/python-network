import getpass
import telnetlib

user = input("Digite o seu usuario: ")
password = getpass.getpass()

lista_routers = open('routers-ip')

for ip in lista_routers:
    ip = ip.strip()
    print('Realizando o Backup do Router ' + (ip))
    HOST = ip
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")

    ler_config = tn.read_all()
    save_config = open('backup-' + HOST, 'w')
    save_config.write(ler_config.decode('ascii'))
    save_config.write('\n')
    save_config.close

print('Backup Completo')
