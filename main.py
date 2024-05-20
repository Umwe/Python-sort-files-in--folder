import os
import shutil

# Function to count files in a folder
def count_files(folder_path):
    return len([name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))])

# Define the path to your main folder
main_folder = "path/to/your/main/folder"

# Iterate through each folder in the main folder
folders = os.listdir(main_folder)

# Dictionary to store folders based on file count
folders_by_count = {}

for folder in folders:
    folder_path = os.path.join(main_folder, folder)
    if os.path.isdir(folder_path):
        file_count = count_files(folder_path)
        if file_count not in folders_by_count:
            folders_by_count[file_count] = [folder]
        else:
            folders_by_count[file_count].append(folder)

# Create new folders and move original folders
for file_count, folders_list in folders_by_count.items():
    new_folder_name = f"{file_count}_files"
    new_folder_path = os.path.join(main_folder, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    for folder in folders_list:
        old_folder_path = os.path.join(main_folder, folder)
        new_folder_path_with_folder = os.path.join(new_folder_path, folder)
        shutil.move(old_folder_path, new_folder_path_with_folder)

print("Folders sorted and grouped based on file count.")
