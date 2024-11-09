import os
import re

def natural_sort_key(filename):
    """
    Generate a sorting key that allows for natural sorting of filenames.
    
    :param filename: The filename to generate the sorting key for.
    :return: A list that can be used as a key for sorting.
    """
    # Split the filename into a list of numbers and strings
    return [int(part) if part.isdigit() else part for part in re.split('(\d+)', filename)]

def list_files_in_directory(directory):
    """
    Lists all files in the specified directory and returns them as a sorted list.

    :param directory: The directory path where to list files from.
    :return: A sorted list of file paths.
    """
    files_list = []

    # Loop through the directory and list all files
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            files_list.append(file_path)
    
    # Sort the list of files by filename using the natural sort key
    return sorted(files_list, key=lambda f: natural_sort_key(os.path.basename(f)))

# Example usage
if __name__ == "__main__":
    # Specify the directory you want to list files from
    directory = r"C:\Users\Sachin_Singh\Desktop\New folder"  # Change this to your directory path

    # List and sort the files in the specified directory
    sorted_files = list_files_in_directory(directory)

    # Print the sorted file paths
    print("Sorted files:")
    for file in sorted_files:
        print(file)
