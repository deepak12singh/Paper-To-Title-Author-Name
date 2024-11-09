import sys

def show_intro_help():
    """Display introductory help message."""
    print("=" * 50)
    print(" Welcome to the DATA_GETER Automation Tool!")
    print("=" * 50)
    print("\nThis tool automates various data-related tasks, including running scripts, setting keys, and more.")
    print("\nUse the commands below to navigate the tool or get help on specific features.")
    print("=" * 50)


def show_detailed_help():
    """Display a more detailed help message with categories."""
    print("=" * 50)
    print(" Detailed Help:")
    print("=" * 50)

    print("\n1. General Commands:")
    print("   - autodata help               : Show this general help message.")
    print("   - autodata -h <command>       : Show help for specific commands.")
    
    print("\n2. Running the Script:")
    print("   - autodata here               : Run the script with the current directory as argument.")
    print("   - This command assumes that your PDF files are stored in the current directory.")

    print("\n3. Setting the Generative AI Key:")
    print("   - autodata set key <key_value>: Set the Generative AI key for the script.")
    print("   - This key is necessary for accessing certain features.")
    
    print("\n4. Example Commands:")
    print("   - autodata help")
    print("   - autodata here")
    print("   - autodata set key <key_value>")
    
    print("=" * 50)


def show_command_help(command):
    """Show help for a specific command."""
    if command == 'run':
        print("\nHelp for 'Run Code' Command:")
        print("=" * 50)
        print("This command starts the main script with the current directory as the argument.")
        print("Use the 'here' argument to specify the directory where your PDF files are stored.")
        print("\nCommand: autodata here")
        print("\nCommon Use Case:")
        print("   - If your PDFs are stored in the same folder as this script, use the command 'autodata here' to run it.")
        print("   - Make sure that the directory path is correct.")
        print("\nTroubleshooting:")
        print("   - If no PDFs are found, ensure the directory contains PDF files.")
        print("=" * 50)
        
    elif command == 'key':
        print("\nHelp for 'Set Key' Command:")
        print("=" * 50)
        print("This command is used to configure the Generative AI key for the script.")
        print("Without the correct key, some script features will not work.")
        print("\nCommand: autodata set key <key_value>")
        print("\nCommon Use Case:")
        print("   - Use this command to set your Generative AI API key.")
        print("   - The key should be a valid API key for the generative model being used.")
        print("\nTroubleshooting:")
        print("   - If you receive an error after setting the key, check if your key is correct.")
        print("   - Ensure there are no extra spaces or characters in the key value.")
        print("=" * 50)
    
    elif command == 'set':
        print("\nHelp for 'Set' Command:")
        print("=" * 50)
        print("The 'set' command is used to configure various settings for the script.")
        print("You can set parameters like the key or other settings.")
        print("\nCommand: autodata set <option> <value>")
        print("\nOptions:")
        print("   - key : Set the API key for the script.")
        print("   - <other_option> : Configure other script options.")
        print("\nExample Usage:")
        print("   autodata set key <your_api_key>")
        print("=" * 50)
    
    else:
        print("\nInvalid command! Type 'autodata help' for general help.")
        print("Try 'autodata -h <command>' for more specific help on a particular command.")


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) == 1:
        show_intro_help()  # Show the intro help
    elif len(sys.argv) == 2 and sys.argv[1] == "help":
        show_detailed_help()  # Show detailed help
    elif len(sys.argv) == 3 and sys.argv[1] == "-h":
        show_command_help(sys.argv[2])  # Show help for a specific command
    else:
        show_detailed_help()


if __name__ == "__main__":
    main()
