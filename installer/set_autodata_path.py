import os
import winreg as reg
import ctypes
import sys

def normalize_path(path):
    return os.path.normpath(path)

def clean_path():
    # Open the registry key for environment variables
    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Environment", 0, reg.KEY_SET_VALUE)

    # Retrieve and clean the current PATH
    current_path = os.environ.get("PATH", "")
    current_path_list = [normalize_path(p.strip()) for p in current_path.split(";") if p.strip() and "REG_EXPAND_SZ" not in p]
    unique_path_list = list(dict.fromkeys(current_path_list))  # Remove duplicates

    # Keep only unique paths that are valid and not too long
    new_path_list = [p for p in unique_path_list if len(p) < 260 and os.path.isdir(p)]
    new_path = ";".join(new_path_list)
    
    # Set the cleaned PATH in the registry
    reg.SetValueEx(reg_key, "PATH", 0, reg.REG_EXPAND_SZ, new_path)
    print("Cleaned and updated PATH in registry. Removed duplicates and shortened paths.")
    
    # Update the current session PATH
    os.environ["PATH"] = new_path
    print("Cleaned and updated PATH in current session.")
    
    # Broadcast environment change to notify other applications
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x1A, 0, "Environment")
    reg.CloseKey(reg_key)



def project_name_to_c_drive_path(project_name):
    bat_file_directory = os.path.join("C:\\", project_name)
    return bat_file_directory

def read_bat_file_get_project_name_to_path(file_path):
    content = ""
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()  # Read the entire content and remove trailing whitespace
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # Extract project name
    try:
        project_name = content.split('=')[1].split('"')[0]
    except IndexError:
        print(f"Unexpected format in {file_path}")
        return None

    # Generate and return the full path
    path_project = project_name_to_c_drive_path(project_name)
    return str(path_project)


def add_to_path(directory):
    # Open the registry key for the environment variables
    reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Environment", 0, reg.KEY_SET_VALUE)
    
    # Retrieve the current PATH variable and add the new path if not already in PATH
    current_path = os.environ.get("PATH", "")
    if directory not in current_path:
        new_path = f"{current_path};{directory}"
        
        # Set the updated PATH in the registry
        reg.SetValueEx(reg_key, "PATH", 0, reg.REG_EXPAND_SZ, new_path)
        print(f"Added {directory} to PATH in registry.")
        
        # Update PATH for the current session
        os.environ["PATH"] = new_path
        print(f"Added {directory} to current session PATH.")
        
        # Broadcast environment change to notify other applications
        ctypes.windll.user32.SendMessageW(0xFFFF, 0x1A, 0, "Environment")
    else:
        print(f"{directory} is already in PATH.")
    
    # Close the registry key
    reg.CloseKey(reg_key)


clean_path()

directory = (sys.argv[1].split('"')[0])

file_name = os.path.join(directory,"installer.bat")
print(file_name)
bat_file_path = read_bat_file_get_project_name_to_path(file_name)
print(bat_file_path)
add_to_path(bat_file_path)