import pyfiglet
import subprocess
import os

class SshManager:

    def __init__(self):
        self.port_number = ""
        self.ssh_remote_connection = ""


    def set_ssh_remote_connection(self):
        # Get the remote username
        remote_username = input("\n[+] Enter the remote username: ")
        # Get the remote user ip.
        remote_ip  = input("[+] Enter the remote ip: ")
        # Get the port number to connect.
        self.port_number = input("[+] Enter the port number or type enter to use the default port 22: ")

        if self.port_number == "":
            self.port_number = "22"

        # Concatenate the remote_username and remote_ip to form: remote_username@remote_ip pattern.
        self.ssh_remote_connection = remote_username + "@" + remote_ip

    # function to show options to user.
    def show_option(self):
        print("[+] Please, select one of the option below: \n")
        print("1 - Connect via ssh\n")
        print("2 - Send file to a remote computer\n")
        print("3 - Start the SSH server\n")
        print("4 - Stop the SSH server\n")
        print("Or ctrl + c to quit\n")
        try:
            # Convert the user option to a number.
            option = int(input())
            # Return the user option.
            return option
        except ValueError:
            print("\n[!] Invalid option!\n")



    def connect_via_ssh(self):
        self.set_ssh_remote_connection()
        # Try to connect via ssh.
        result = subprocess.run(["ssh", "-p", self.port_number, self.ssh_remote_connection], stderr=subprocess.PIPE)
        # Verify if connection was refused.
        if "Connection refused" in str(result.stderr):
            print("\n[!] Remote connection refused.\nPlease, ensure that the ssh service is running in the remote computer!\nAnd verify if the " + str(self.port_number) + " is the right port.\n")
        elif "Bad port" in str(result.stderr):
            print("\n[!] Please enter a valid positive integer for the port number.")

    def send_file_via_ssh(self):
        filename = input("\n[+] Enter the filename: ")
        if os.path.isfile(filename):
            self.set_ssh_remote_connection()
            remote_path = self.ssh_remote_connection + ":~"
            result = subprocess.run(["scp", "-P", self.port_number, filename, remote_path], stderr=subprocess.PIPE)
            if "Connection refused" in str(result.stderr):
                print("\n[!] Remote connection refused.\nPlease, ensure that the ssh service is running in the remote computer!")
        else:
            print("\n[!] Please enter a valid file!")

    def start_ssh_server(self):
        print("\n[+] Starting SSH server....")
        subprocess.run(["systemctl", "start", "sshd"])
        print("\n[+] SSH server started!")
    def stop_ssh_server(self):
        print("\n[+] Stopping SSH server....")
        subprocess.run(["systemctl", "stop", "sshd"])
        print("\n[+] SSH server stopped!")

    def show_title(self):
        # Clear the screen
        os.system("clear")
        # Prepares the title.
        ascii_title = pyfiglet.figlet_format("SSH MANAGER", font="slant")
        # Shows the title.
        print("\n")
        print("-" * 68)
        print("")
        print(ascii_title)
        print("-" * 68)
        print("\n")
