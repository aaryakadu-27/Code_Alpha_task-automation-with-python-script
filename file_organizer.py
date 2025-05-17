import os
import shutil

# Define the source directory
source_dir = os.path.expanduser("~/Downloads")  # Change this if needed

# Define file type categories and corresponding extensions
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Software": [".exe", ".msi", ".dmg"],
    "Code": [".py", ".java", ".cpp", ".c", ".html", ".js", ".css"]
}

# Create target folders if not already present
for folder in file_types.keys():
    folder_path = os.path.join(source_dir, folder)
    os.makedirs(folder_path, exist_ok=True)

# Organize files
for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(file)

    # Move the file to the corresponding folder
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            target_path = os.path.join(source_dir, folder, file)
            shutil.move(file_path, target_path)
            print(f"Moved: {file} → {folder}/")
            break
