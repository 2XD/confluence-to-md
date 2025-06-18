import os

# Comment out Azure import for now
# from azure.storage.blob import BlobServiceClient

def upload_to_blob(content, blob_name, metadata, config):
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)

    # Write to local file instead of uploading
    local_path = os.path.join(output_dir, blob_name)
    with open(local_path, "w", encoding="utf-8") as file:
        file.write(content)

    # Log metadata as a JSON-style file
    meta_path = os.path.join(output_dir, f"{blob_name}.meta.txt")
    with open(meta_path, "w", encoding="utf-8") as metafile:
        for key, value in metadata.items():
            metafile.write(f"{key}: {value}\n")

    print(f"[DEV MODE] Stored '{blob_name}' locally at '{local_path}' with metadata: {metadata}")
