import shutil
from pathlib import Path

def copy_file(source_path: str, destination_path: str) -> None:
    """
    Copy a file from source_path to destination_path.

    Args:
    - source_path (str): The path of the file to copy.
    - destination_path (str): The path where the file should be copied.

    Raises:
    - FileNotFoundError: If the source file doesn't exist.
    - Exception: For any other exceptions during the copy process.
    """
    try:
        # Check if the source file exists
        if not Path(source_path).is_file():
            raise FileNotFoundError(f"The file {source_path} does not exist.")

        # Copy the file to the destination
        shutil.copy(source_path, destination_path)
        # print(f"File copied successfully from {source_path} to {destination_path}")
    except Exception as e:
        print(f"An error occurred: {e}")





# Example usage
# copy_file("path/to/source/file.txt", "path/to/destination/file.txt")
