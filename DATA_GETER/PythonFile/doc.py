from docx2pdf import convert
import os

def change_name_experience(file_path):
    """
    Modifies the file path to have a .pdf extension.
    
    Parameters:
    file_path (str): The original file path of the document.
    
    Returns:
    str: The file path with the .pdf extension.
    """
    try:
        # Split the file path into base name and extension
        base, _ = os.path.splitext(file_path)
        # Concatenate base with .pdf to form the new file path
        new_file_path = f"{base}.pdf"
        return new_file_path
    except Exception as e:
        # Print an error message if an exception occurs
        print('Error found:', e)

def Doc_To_Pdf(file_path):
    """
    Converts a .docx file to .pdf format and updates the file path.
    
    Parameters:
    file_path (str): The original file path of the .docx document.
    
    Returns:
    str: The file path of the converted .pdf document.
    """
    try:
        # Convert the provided .docx file to .pdf format
        convert(file_path)
        # Update the file path to reflect the .pdf extension
        file_path = change_name_experience(file_path)
        return file_path
    except Exception as e:
        # Print an error message if an exception occurs
        print('Error found:', e)
        return ''

# Entry point for the script
if __name__ == "__main__":
    # Define the original file path for the .docx file
    file_path = r"C:\Users\Sachin_Singh\Desktop\New A.S\data_doc\128.docx"
    # Convert the file to PDF and retrieve the new file path
    new_file_path = Doc_To_Pdf(file_path)
    # Print the file path of the converted PDF
    print(new_file_path)
