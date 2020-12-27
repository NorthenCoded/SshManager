import pyfiglet
import subprocess

# function to show options to user.
def show_option():
    print("[+] Please, select one of the option below: \n")
    print("1 - Connect via ssh\n")
    try:
        # Convert the user option to a number.
        option = int(input())
        # Return the user option.
        return option
    except ValueError:
        print("\n[!] Invalid option!")



def connect_via_ssh():
    # Get the remote username.
    remote_username = input("\n[+] Enter the remote username: ")
    # Get the remote user ip.
    remote_ip  = input("[+] Enter the remote ip: ")
    # Get the port number to connect.
    port_number = input("[+] Enter the port number: ")
    # Concatenate the remote_username and remote_ip to form: remote_username@remote_ip pattern.
    ssh_remote_connection = remote_username + "@" + remote_ip
    # Try to connect via ssh.
    result = subprocess.run(["ssh", "-p", port_number, ssh_remote_connection], stderr=subprocess.PIPE)
    # Verify if connection was refused.
    if "Connection refused" in str(result.stderr):
        print("\n[!] Remote connection refused.\nPlease, ensure that the ssh service is running in the remote computer!")

# Prepares the title.
ascii_title = pyfiglet.figlet_format("SSH MANAGER", font="slant")
# Shows the title.
print("\n")
print("-" * 65)
print("")
print(ascii_title)
print("-" * 65)
print("\n")
try:
    # Calls the function to receive user option.
    choice_option = show_option()
    if choice_option == 1:
        connect_via_ssh()
except KeyboardInterrupt:
    print("\nExiting....")
