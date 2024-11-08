import PyPDF2
import google.generativeai as genai
import json
from DATAGETER_PROJECT.confilg import *
import os
from google.api_core.exceptions import ResourceExhausted
from .countdown_timer import start_countdown
from .readingPdf import read_first_page

# Configure the API key (replace with your actual key)
genai.configure(api_key=GENERATIVE_AI_KEY)

def data_Extrater_commond(text,file_name):
    prompt = f"""
    Extract the following information from the given data:
    Paper Title, Author Name, Email Id, Corresponding Author, Corresponding Author Email.
    Data: '{text}'
    email id must contain @ 
    Output format:
    {{
        "Paper_Title": "An Efficient Approach for Decentralized Web Messaging using WebRTC",
        "Author_NameAnd_Email": {{
            "Manisha Kasar": "mmkasar@bvucoep.edu.in",
            "Trupti Suryawanshi": "tvsuryawanshi@bvucoep.edu.in",
            "Pranoti Kavimandan": "pskavimandan@bvucoep.edu.in",
            "Snehal Chaudhari": "sdchaudhary@bvucoep.edu.in",
            "Sachin Pratap Singh Raghav": "04717711922_ds@vips.edu",
            "Neelansh Sharma": "02017711922_ds@vips.edu"
            "Aryaveer Singh":"01217711922_ds@vips.edu"
            "Ayush Shrotriya": "01717711922_ds@vips.edu",
        }},
        "Corresponding_Author": "Manisha Kasar",
        "Corresponding_Author_Email": "mmkasar@bvucoep.edu.in"
    }}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
   

    # Handle ResourceExhausted error and retry after delay
    while True:
        try:
            response = model.generate_content(prompt)
            break  # Exit loop if successful
        except ResourceExhausted:
            print("Quota exhausted. Retrying after 60 seconds...",file_name)
            start_countdown(60)  # Wait for 60 seconds before retrying
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""

    # Extract the generated content
    return response.text.strip()



def convert_to_dictionary(json_string):
    try:
        json_string = json_string.split('```')[1].split('json\n')[1]
        data_dict = json.loads(json_string)
        return data_dict
    except (json.JSONDecodeError, IndexError) as e:
        print("Error: Unable to parse JSON.", e)
        return {}


def Error_file(message, output_path,save_file_name='Error.txt'):
    file_name = output_path.split('\\')[-1]
    output_directory = os.path.dirname(output_path)

    output_directory = os.path.join(output_directory, "output")
    os.makedirs(output_directory, exist_ok=True)

    error_file_path = os.path.join(output_directory, save_file_name)
    

    with open(error_file_path, 'a') as error_file:
        error_file.write(f"{file_name}: {message}\n")

        

def DataGeter(file_path):
    file_name = file_path.split('\\')[-1]
    first_page_content = read_first_page(file_path)

    if not first_page_content:
        Error_file("This file is in image format or has no readable text.", file_path)
        print(file_name, "This file is in image format or has no readable text.")
        return ''

    extracted_info = data_Extrater_commond(first_page_content,file_name)
    data_dict = convert_to_dictionary(extracted_info)

    if not data_dict:
        Error_file("Failed to parse the generated content.", file_path)
        return "Failed to parse the generated content."

    data_dict["Paper_No"] = file_name.split('.')[0]
    return data_dict

# Example usage
if __name__ == "__main__":
    file_name = "27.pdf"
    pdf_file_path = file_name
    first_page_content = read_first_page(pdf_file_path)
    extracted_info = data_Extrater_commond(first_page_content)
    data_dict = convert_to_dictionary(extracted_info)
    data_dict["Paper_No"] = file_name.split('.')[0]
    print(data_dict)

