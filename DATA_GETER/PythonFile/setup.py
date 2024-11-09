import sys
GENERATIVE_AI_KEY = 'AIzaSyDDxDW0vukR0mrwrR_4b2CMqnkSwA7T6H4'
def find_line_number(filename, search_key):
    """Finds and returns the line numbers where `search_key` appears in the file. 
    If not found, returns the line number after the last line."""
    line_numbers = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if search_key in line:
                    line_numbers.append(line_number)
        
        # If search_key was found, return the list of line numbers
        if line_numbers:
            return line_numbers
        else:
            # If not found, return the next line number after the last line
            return [len(lines) + 1]
    except FileNotFoundError:
        return f"The file {filename} was not found."


def delete_line_by_number(filename, line_number):
    """Deletes the line at the specified line number in the file."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        
        # Check if the given line number is valid
        if 1 <= line_number <= len(lines):
            # Remove the specified line (adjust for 0-based index)
            del lines[line_number - 1]
            
            # Write the modified content back to the file
            with open(filename, "w") as file:
                file.writelines(lines)
            
            print(f"Line {line_number} has been deleted from {filename}.")
        else:
            print(f"Line {line_number} is out of range. The file has only {len(lines)} lines.")
            
    except FileNotFoundError:
        print(f"The file {filename} was not found.")


def insert_line_at_number(filename, line_number, new_data):
    """Inserts `new_data` at the specified line number in the file."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
        
        # Adjust line_number for 1-based indexing
        if line_number <= 0:
            print("Line number should be greater than 0.")
            return

        # Insert the new line at the specified position
        if line_number <= len(lines):
            lines.insert(line_number - 1, new_data + "\n")
        else:
            # If line_number is beyond the end of the file, append the new data
            lines.append(new_data + "\n")
        
        # Write the updated lines back to the file
        with open(filename, "w") as file:
            file.writelines(lines)
        
        print(f"Inserted data at line {line_number} in {filename}.")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")

def Set_GENERATIVE_AI_KEY_(key='None'):
    # Usage example
    filename = "config.py"
    line_numbers = find_line_number(filename, "GENERATIVE_AI_KEY")

    # If the search_key was not found, line_numbers will have the next available line number
    line_number = line_numbers[-1]
    print(f"Line number to insert: {line_number}")

    try:
        # If line_number is not in range or invalid, avoid deletion attempt
        delete_line_by_number(filename, line_number)
    except Exception as e:
        print(f"Error in deletion: {e}")

    # Insert the new data at the specified line number
    insert_line_at_number(filename, line_number, f"GENERATIVE_AI_KEY = '{key}'")
    print('Succefuly update GENERATIVE_AI_KEY = ',key)

key = sys.argv[1]
if __name__ == '__main__':
    Set_GENERATIVE_AI_KEY_(key)