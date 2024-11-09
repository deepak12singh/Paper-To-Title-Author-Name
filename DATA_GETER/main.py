print("Requirements Library Loading .....")
import sys
import os
import PyPDF2  # Ensure PyPDF2 is imported for PdfReadError
import time
from PythonFile.getfile_data import DataGeter, Error_file
from PythonFile.getfiles import list_files_in_directory
from PythonFile.SaveDataXL import save_to_excel
from PythonFile.file_to_path import create_folder_for_file
from PythonFile.copy import copy_file
from PythonFile.doc import Doc_To_Pdf

try:
    from google.api_core.exceptions import ResourceExhausted
except ImportError:
    ResourceExhausted = None

print("Data extraction starting...")

def Erro_file_copy(file_path, Folder_name='Extance change Files Error'):
    """Creates a folder and copies a file into it for error handling."""
    file_path_input, file_path_output = create_folder_for_file(file_path, Folder_name)
    Error_file(Folder_name,file_path)
    copy_file(file_path_input, file_path_output)
    print('Error file copied to:', Folder_name)

directory = sys.argv[1]
list_of_files = list_files_in_directory(directory=directory)

fileRemov = False
for file_path in list_of_files:
    file_name = os.path.basename(file_path)
    try:
        # Check for valid file extensions and skip temporary or error files
        if not (file_path.endswith(".pdf") or file_path.endswith(".docx") or file_path.endswith(".xlsx")) or "~$" in file_name:
            print("Skipping non-target file:", file_name)
            Erro_file_copy(file_path)
            continue

        # Convert .docx files to PDF
        if file_path.endswith(".docx"):
            file_path_ = file_path
            file_path = Doc_To_Pdf(file_path)
            if file_path:
                fileRemov = True
            else:
                Erro_file_copy(file_path_, 'Permissions Issue')
                fileRemov = False
                continue

        # Data extraction
        data = DataGeter(file_path)
        if not data:
            # Handle files with images that may require different processing
            file_path_input, file_path_output = create_folder_for_file(file_path, 'Image files in PDF')
            copy_file(file_path_input, file_path_output)
            continue
        save_to_excel(data, directory)
        if fileRemov:
            os.remove(file_path)
            fileRemov = False

    except PyPDF2.errors.PdfReadError:
        Error_file("PDF file is corrupt or has no EOF marker.", file_path)
        
    except PermissionError:
        Error_file("Permission denied. File might be open in another application.", file_path)
        
    except ResourceExhausted:
        print("Quota exhausted. Retrying after 60 seconds...", file_name)
        time.sleep(60)
        
    except Exception as e:
        Error_file(f"Unexpected error: {str(e)}", file_path)
        print(f"Error with file {file_path}: {e}")
