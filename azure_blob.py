import os

def upload_to_blob(content: str, blob_name: str, metadata: dict, config: dict):
    """
    For local dev, saves content as a markdown file and metadata as a .meta.txt file
    preserving folder structure under ./output.

    Args:
        content (str): Markdown content to save
        blob_name (str): Path including folders + filename (e.g. "Team/Doc.md")
        metadata (dict): Metadata dictionary
        config (dict): Config dictionary (not used here but kept for signature)
    """
    output_dir = "./output"
    full_path = os.path.join(output_dir, blob_name)

    # Create intermediate directories if not exist
    folder = os.path.dirname(full_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    # Write markdown content
    with open(full_path, "w", encoding="utf-8") as file:
        file.write(content)

    # Write metadata alongside markdown file
    meta_path = full_path + ".meta.txt"
    with open(meta_path, "w", encoding="utf-8") as metafile:
        for key, value in metadata.items():
            metafile.write(f"{key}: {value}\n")

    print(f"[DEV MODE] Stored '{blob_name}' locally at '{full_path}' with metadata: {metadata}")
