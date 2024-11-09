import pandas as pd
import os
from .getfile_data import Error_file

def save_to_excel(data_dict, directory):
    # Prepare a list to store rows for the DataFrame
    rows = []

    # Extract common data
    paper_no = data_dict.get('Paper_No', '')
    paper_title = data_dict.get('Paper_Title', '')
    corresponding_author = data_dict.get('Corresponding_Author', '')
    corresponding_author_email = data_dict.get('Corresponding_Author_Email', '')

    # Get author details
    author_details = data_dict.get('Author_NameAnd_Email', {})

    # Create a row for each author in the dictionary
    for author_name, author_email in author_details.items():
        row = {
            'Paper_No': paper_no,
            'Paper_Title': paper_title,
            'Author_Name': author_name,
            'Author_Email': author_email,
            'Corresponding_Author': corresponding_author,
            'Corresponding_Author_Email': corresponding_author_email
        }
        rows.append(row)

    # Convert the list of dictionaries into a DataFrame
    new_data_df = pd.DataFrame(rows)

    # Create the 'output' folder inside the specified directory
    output_folder = os.path.join(directory, "output")
    os.makedirs(output_folder, exist_ok=True)

    # Set the output file path
    output_file_path = os.path.join(output_folder, "output.xlsx")

    # If the file exists, read the existing data and append the new data
    if os.path.exists(output_file_path):
        existing_data_df = pd.read_excel(output_file_path)
        combined_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)
    else:
        # If the file doesn't exist, the combined data is just the new data
        combined_df = new_data_df

    # Save the combined DataFrame to the specified Excel file path
    combined_df.to_excel(output_file_path, index=False)
    Error_file(f'Successfuly save data',os.path.join(directory,paper_no),'successfuly.txt')
    print(f"Data appended and saved to {paper_no}")

# Example usage
if __name__ == "__main__":
    # Given data in dictionary format
    data = {
        'Paper_Title': 'Face Identification and Categorization with and without Mask utilizing MTCNN and OpenCV for accessing Bank Locker Facility',
        'Author_NameAnd_Email': {
            'Ms. R.Monica Lakshmi': 'monica.ramar@gmail.com',
            'Dr.K.Ramar': 'kramar.einstein@gmail.com',
            'Nikita Devendran': 'ucb20128@rmd.ac.in',
            'Deepika L.P': 'ucb20111@rmd.ac.in',
            'Mounika.S': 'ucb20126@rmd.ac.in'
        },
        'Corresponding_Author': 'Ms. R.Monica Lakshmi',
        'Corresponding_Author_Email': 'monica.ramar@gmail.com',
        'Paper_No': '27'
    }

    # Specify the directory where the output folder should be created
    given_directory = "C:/Users/Sachin_Singh/Desktop/AdityaSir/0001"
    save_to_excel(data, given_directory)





