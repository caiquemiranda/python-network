import telnetlib
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class CiscoTelnetConnection:
    def __init__(self, host, username, password, enable_password=None):
        """
        Initialize Cisco router telnet connection.

        Args:
            host: IP address or hostname of Cisco router
            username: Telnet username
            password: Telnet password
            enable_password: Enable mode password (optional)
        """
        self.host = host
        self.username = username
        self.password = password
        self.enable_password = enable_password
        self.connection = None
        self.timeout = 10

    def connect(self):
        """Establish telnet connection to Cisco router"""
        try:
            self.connection = telnetlib.Telnet(self.host, timeout=self.timeout)
            print(f"Connected to {self.host}")

            # Wait for username prompt
            output = self.connection.read_until(
                b"Username: ", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))

            # Send username
            self.connection.write(self.username.encode() + b"\n")
            time.sleep(0.5)

            # Wait for password prompt
            output = self.connection.read_until(
                b"Password: ", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))

            # Send password
            self.connection.write(self.password.encode() + b"\n")
            time.sleep(0.5)

            # Read prompt
            output = self.connection.read_until(b">", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))
            print("Authentication successful!")

            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def enter_enable_mode(self):
        """Enter enable mode on Cisco router"""
        if not self.enable_password:
            print("Enable password not provided")
            return False

        try:
            self.connection.write(b"enable\n")
            time.sleep(0.5)

            output = self.connection.read_until(
                b"Password: ", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))

            self.connection.write(self.enable_password.encode() + b"\n")
            time.sleep(0.5)

            output = self.connection.read_until(b"#", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))
            print("Entered enable mode!")

            return True
        except Exception as e:
            print(f"Failed to enter enable mode: {e}")
            return False

    def send_command(self, command):
        """Send a command and return the output"""
        try:
            self.connection.write(command.encode() + b"\n")
            time.sleep(0.5)

            output = self.connection.read_very_eager()
            return output.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Command failed: {e}")
            return None

    def disconnect(self):
        """Close telnet connection"""
        if self.connection:
            self.connection.close()
            print("Connection closed")


# Example usage
if __name__ == "__main__":

    ROUTER_IP = os.getenv("ROUTER_IP")
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    ENABLE_PASSWORD = os.getenv("ENABLE_PASSWORD")

    # Create connection
    cisco = CiscoTelnetConnection(
        ROUTER_IP, USERNAME, PASSWORD, ENABLE_PASSWORD)

    # Connect
    if cisco.connect():
        # Enter enable mode
        cisco.enter_enable_mode()

        # Send commands
        result = cisco.send_command("show version")
        print(result)

        result = cisco.send_command("show ip interface brief")
        print(result)

        # Disconnect
        cisco.disconnect()
    else:
        print("Failed to establish connection")
