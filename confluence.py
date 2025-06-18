import os
import requests
from markdownify import markdownify as md
from azure_blob import upload_to_blob
from datetime import datetime

def get_page_content(page_id, config):
    url = f"{config['CONFLUENCE_BASE_URL']}/{page_id}"
    headers = {
        'Authorization': f"Bearer {config['CONFLUENCE_API_TOKEN']}",
        'Accept': 'application/json'
    }
    params = {'expand': 'body.storage,version'}
    response = requests.get(url, headers=headers, params=params, verify=False)
    response.raise_for_status()
    data = response.json()
    return {
        "id": page_id,
        "title": data["title"],
        "html": data["body"]["storage"]["value"],
        "created": data["version"]["when"]
    }

def get_child_pages(page_id, config):
    url = f"{config['CONFLUENCE_BASE_URL']}/{page_id}/child/page"
    headers = {
        'Authorization': f"Bearer {config['CONFLUENCE_API_TOKEN']}",
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    return response.json().get('results', [])

def process_page(page_id, config, path=''):
    page = get_page_content(page_id, config)
    md_content = md(page["html"])
    clean_title = page["title"].replace("/", "-").replace("\\", "-")
    blob_path = os.path.join(path, f"{clean_title}.md").replace("\\", "/")

    metadata = {
        'created_date': datetime.fromisoformat(page["created"].replace("Z", "+00:00")).strftime('%Y-%m-%d'),
        'source_page': f"{config['CONFLUENCE_BASE_URL']}/{page_id}"
    }

    upload_to_blob(md_content, blob_path, metadata, config)

    for child in get_child_pages(page_id, config):
        process_page(child["id"], config, os.path.join(path, clean_title))
