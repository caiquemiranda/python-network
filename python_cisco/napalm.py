from napalm import get_network_driver
import json

driver = get_network_driver("ios")

device = driver(
        hostname="192.168.0.101",
        username="miranda",
        password="cisco",
        optional_args={"port": 22},
    )
device.open()

output = device.get_arp_table()
print(json.dumps(output, indent=4))