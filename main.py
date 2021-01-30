import ssh_manager

try:
    # Getting a SshManager object.
    ssh_manager = ssh_manager.SshManager()
    ssh_manager.show_title()
    while True:
         # Calls the function to receive user option.
        choice_option = ssh_manager.show_option()
        if choice_option == 1:
            ssh_manager.connect_via_ssh()
        elif choice_option == 2:
            ssh_manager.send_file_via_ssh()
        elif choice_option == 3:
            ssh_manager.start_ssh_server()
        elif choice_option == 4:
            ssh_manager.stop_ssh_server()

except KeyboardInterrupt:
    print("\nExiting....")
