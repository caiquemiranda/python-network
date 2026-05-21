import telnetlib
import time
from dotenv import load_dotenv

load_dotenv()


class CiscoTelnetConnection:
    def __init__(self, host, username, password, enable_password=None):
        self.host = host
        self.username = username
        self.password = password
        self.enable_password = enable_password
        self.connection = None
        self.timeout = 10

    def connect(self):
        try:
            self.connection = telnetlib.Telnet(self.host, timeout=self.timeout)
            print(f"Connected to {self.host}")
            
            output = self.connection.read_until(
                b"Username: ", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))
            
            self.connection.write(self.username.encode() + b"\n")
            time.sleep(0.5)

            output = self.connection.read_until(
                b"Password: ", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))
            
            self.connection.write(self.password.encode() + b"\n")
            time.sleep(0.5)

            output = self.connection.read_until(b">", timeout=self.timeout)
            print(output.decode('utf-8', errors='ignore'))
            print("Authentication successful!")

            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def enter_enable_mode(self):

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

        try:
            self.connection.write(command.encode() + b"\n")
            time.sleep(0.5)

            output = self.connection.read_very_eager()
            return output.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Command failed: {e}")
            return None

    def disconnect(self):

        if self.connection:
            self.connection.close()
            print("Connection closed")


