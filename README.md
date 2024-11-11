# Paper To Title Author Name and Corresponding Authors

This project extracts metadata from research papers, such as the paper title, authors' names and emails, and corresponding author information from PDF and DOCX files. The extracted data is saved into an Excel file for easy access and organization.

## Features

- **Extract Paper Metadata**: Automatically parse the title, authors, and corresponding author from research papers in PDF or DOCX formats.
- **Structured Output**: Data is organized in a format that includes:
  - `Paper_No`: Unique identifier for each paper.
  - `Paper_Title`: Title of the paper.
  - `Author_Name`: Names of all authors.
  - `Author_Email`: Email addresses of each author.
  - `Corresponding_Author`: Name of the corresponding author.
  - `Corresponding_Author_Email`: Email of the corresponding author.
- **Excel Export**: Outputs all extracted information into an Excel file for streamlined analysis and reporting.

## Requirements
- **Python**: Version 3.8 or higher is required.
## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/deepak12singh/Paper-To-Title-Author-Name.git
    cd Paper-To-Title-Author-Name
    ```

2. **Run the Installer**:
   - Execute the `installer.bat` file to install all necessary dependencies and set up the project.
   
   ```bash
   installer.bat
   ```

## Usage

1. **Navigate to the Folder Containing Your Files**:
   - Go to the directory where your PDF and DOCX files are located. For example:
     ```bash
     cd C:\Users\....\Paper-To-Title-Author-Name\testing
     ```

2. **Run the Command to Set Google Generative AI  API Key**:
   - Use the following command to Set API Key:
     ```bash
     autodata set key <key_value>
     ```
3. **Run the Command to Start Data Extraction**:
   - Use the following command to start the data extraction process:
     ```bash
     autodata here
     ```

3. **View the Output**:
   - After running the command, the script will process each file in the folder and output data to an Excel file. You will see the progress for each file processed in the console.

### Example Console Output

```
Requirements Library Loading .....
Data extraction starting...
Data appended and saved to 12
Data appended and saved to 22
Data appended and saved to 128
Data appended and saved to 129
100%
```

This output confirms that each file is processed and saved with a unique identifier.

## License

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


--- 

Simply copy and paste this content into your README.md file. Let me know if you need any further adjustments!
