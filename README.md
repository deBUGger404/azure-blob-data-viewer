# Azure Blob Storage PDF Manager

## Purpose
This Streamlit application is designed to manage PDF files stored in Azure Blob Storage. It allows users to upload PDF files to a specified container, as well as to display and download PDF files from the Azure Blob Storage.

## Functionality
- **Upload PDF**: Users can upload PDF files to a designated container in Azure Blob Storage.
- **Display and Download PDF**: Users can select a PDF file from the storage, display it within the application, and download it to their local system.

## How to Use
1. **Installation**: Ensure you have Python installed in your environment. You can install the necessary dependencies by running `pip install -r requirements.txt`.
2. **Azure Blob Connection String**: Provide your Azure Blob Storage connection string in the sidebar. This allows the application to interact with your Azure Blob Storage account.
3. **Upload PDF**: Navigate to the "Upload PDF" tab. Choose a PDF file using the file uploader, then click the "Upload PDF" button. The file will be uploaded to the specified container in Azure Blob Storage.
4. **Display and Download PDF**: Go to the "Display PDF" tab. Select a PDF file from the dropdown menu. Click the "Display PDF" button to view the PDF within the application. To download the PDF file, click the "Download PDF" button. The file will be downloaded to your local system.

## Running the Application Locally
1. Clone this repository to your local machine.
2. Navigate to the directory containing the `README.md` file.
3. Open a terminal or command prompt.
4. Run the Streamlit application by executing the following command:
   ```python
   streamlit run app.py
   ```

6. Access the application in your web browser by visiting the URL provided in the terminal.
