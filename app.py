import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from streamlit_pdf_viewer import pdf_viewer

def upload_pdf_to_blob(blob_service_client, file, container_name, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(file, overwrite=True)
    st.success(f"Uploaded {blob_name} to blob storage in container {container_name}.")

def read_pdf_from_blob(blob_service_client, container_name, blob_name):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_data = blob_client.download_blob()
    pdf_content = blob_data.readall()
    return pdf_content

# Streamlit App
st.title("Azure Blob Storage PDF Manager")

container_name = "upload"  # Name of the container in Azure Blob Storage
user_folder = "rakesh"  # Simulating a user-specific folder

# Sidebar Instruction
st.sidebar.markdown("""
### Instructions
1. Enter your Azure Blob connection string.
2. Choose an operation: Upload PDF or Display PDF.
3. Follow the prompts.
""")

# Initialize the BlobServiceClient
blob_string = st.sidebar.text_input("Enter Azure Blob String:")
if blob_string:
    blob_service_client = BlobServiceClient.from_connection_string(blob_string)
else:
    blob_service_client = None
    st.error("Please enter a valid Azure Blob string.")
    st.stop()

tab1, tab2 = st.tabs(["Upload PDF", "Display PDF"])

with tab1:
    st.header("Upload PDF to Azure Blob Storage")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file and st.button("Upload PDF") and blob_service_client:
        blob_name = os.path.join(user_folder, uploaded_file.name)
        upload_pdf_to_blob(blob_service_client, uploaded_file, container_name, blob_name)

with tab2:
    st.header("Display PDF from Azure Blob Storage")
    # List files in directory
    file_content = None
    files_in_directory = [item.name for item in blob_service_client.get_container_client(container_name).list_blobs()]
    blob_name = st.selectbox("Select Blob Name to Display", files_in_directory)
    if blob_name:
        download_path = os.path.join(blob_name)
        file_content = read_pdf_from_blob(blob_service_client, container_name, blob_name)
        st.download_button('Download PDF', file_content, blob_name.split('/')[-1], key=blob_name)
        st.toast(f"PDF displayed and downloaded successfully.")
        pdf_viewer(file_content)
        st.toast(f"Loaded {blob_name} from blob storage.")
