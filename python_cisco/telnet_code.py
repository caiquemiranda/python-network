import os
from conection import CiscoTelnetConnection


ROUTER_IP = os.getenv("ROUTER_IP")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
ENABLE_PASSWORD = os.getenv("ENABLE_PASSWORD")

cisco = CiscoTelnetConnection(
    ROUTER_IP, USERNAME, PASSWORD, ENABLE_PASSWORD)

if cisco.connect():
    cisco.enter_enable_mode()
    result = cisco.send_command("show version")
    print(result)
    result = cisco.send_command("show ip interface brief")
    print(result)
    cisco.disconnect()
else:
    print("Failed to establish connection")
