import os
from urllib.parse import quote


def get_file_paths(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        # Check if .git folder is in the list of directories
        if '.git' in dirs:
            dirs.remove('.git')  # Remove .git folder from the list of directories
        if 'main.py' in files:
            files.remove('main.py')
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(string_to_URL_encoded(clean_file_name(folder_path, file_path)))
    return file_paths


def clean_file_name(folder_path, full_path):
    return full_path.replace(folder_path + '\\', '').replace('\\', '/')


def string_to_URL_encoded(str):
    return quote(str)


# Example usage:
folder_path = "C:/Users/adamp/VsCode/Fonts"
file_paths = get_file_paths(folder_path)
print(file_paths)
