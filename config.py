import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {
        'CONFLUENCE_API_TOKEN': os.environ['CONFLUENCE_API_TOKEN'],
        'CONFLUENCE_BASE_URL': os.environ['CONFLUENCE_BASE_URL'],
        'AZURE_STORAGE_CONNECTION_STRING': os.environ['AZURE_STORAGE_CONNECTION_STRING'],
        'AZURE_CONTAINER_NAME': os.environ['AZURE_CONTAINER_NAME']
    }
