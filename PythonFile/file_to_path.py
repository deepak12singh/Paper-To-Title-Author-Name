from pathlib import Path
import os



def create_folder_for_file(file_name_or_full_path: str, create_rootfolder_name_wherea_file='doc') -> tuple:
    """
    Creates a specified folder inside the directory where the file is located,
    and places the file inside the created folder.

    Args:
    - file_name_or_full_path (str): The file name or full file path where the folder should be created.
    - create_rootfolder_name_wherea_file (str): The name of the folder to create (default is 'doc').

    Returns:
    - tuple: (file_path, created_folder_path_with_file)
    """
    # Get the directory of the file
    file_path = os.path.dirname(file_name_or_full_path)
    
    # Define the folder path inside the file directory
    folder_path = Path(file_path) / 'output' / 'Files' / create_rootfolder_name_wherea_file
    
    try:
        # Create the folder if it doesn't exist
        folder_path.mkdir(parents=True, exist_ok=True)
        
        # Define the file path inside the new folder
        new_file_path = folder_path / Path(file_name_or_full_path).name
        
        # Return both the original file path and the file path inside the created folder
        return str(Path(file_name_or_full_path).resolve()), str(new_file_path.resolve())
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return "", ""

