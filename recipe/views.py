import zipfile
import os

zip_path = "/mnt/data/5.zip"
extract_path = "/mnt/data/project_5"

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

os.listdir(extract_path)
