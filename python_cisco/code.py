"""Base Cisco network helper code.

This module provides a small starting point for Cisco-oriented network
automation scripts.
"""

from dataclasses import dataclass


@dataclass
class CiscoDevice:
	host: str
	username: str
	password: str
	port: int = 22
	timeout: int = 10


class CiscoNetworkClient:
	def __init__(self, device: CiscoDevice):
		self.device = device
		self._connection = None

	def connect(self) -> None:
		"""Connect to the Cisco device."""
		raise NotImplementedError("Connect logic not implemented yet")

	def disconnect(self) -> None:
		"""Close the device connection if one exists."""
		if self._connection:
			close = getattr(self._connection, "disconnect", None) or getattr(
				self._connection, "close", None
			)
			if callable(close):
				close()
		self._connection = None

	def send_command(self, command: str) -> str:
		"""Send a command to the device and return its output."""
		if not self._connection:
			raise RuntimeError("Not connected to any device")

		if hasattr(self._connection, "send_command"):
			return self._connection.send_command(command)
		if hasattr(self._connection, "run"):
			return self._connection.run(command)

		raise NotImplementedError("Connected object does not support commands")


def main() -> None:
	"""Example entry point."""
	device = CiscoDevice(host="192.0.2.1", username="admin", password="password")
	client = CiscoNetworkClient(device)
	print(f"Prepared client for {device.host}:{device.port}")


if __name__ == "__main__":
	main()
