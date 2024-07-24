import subprocess

def format_path(path):
    """
    Remove any surrounding quotes from the path.
    
    :param path: The original path string.
    :return: The formatted path string without surrounding quotes.
    """
    # Remove surrounding quotes if they exist
    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1]
    return path

def block_firewall_rule(program_path, program_name):
    """
    Adds an outbound rule in the Windows Firewall to block the given program.
    
    :param program_path: Path to the program's executable.
    :param program_name: Name of the program for the rule.
    """
    # Format the path to remove surrounding quotes
    program_path = format_path(program_path)
    
    try:
        # Construct the netsh command to block an outbound firewall rule
        command = [
            "netsh", "advfirewall", "firewall", "add", "rule",
            f"name={program_name}",
            "dir=out",
            "action=block",
            f"program={program_path}",
            "enable=yes"
        ]
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Outbound rule to block {program_name} added successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"Failed to add outbound block rule: {e}")

def main():
    """
    Main function to execute the CLI application.
    """
    # Ask the user for the program path and name
    program_path = input("Enter the full path of the program to block: ")
    program_name = input("Enter the program name: ")
    
    # Block the program in the firewall
    block_firewall_rule(program_path, program_name)

if __name__ == "__main__":
    main()
