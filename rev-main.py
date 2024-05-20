import os
import shutil

# Define the path to your main folder
main_folder = "path/to/your/main/folder"

# Function to move folders and their content back to the main folder
def move_folders_back():
    # Get a list of subfolders in the main folder
    subfolders = [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]
    
    for subfolder in subfolders:
        subfolder_path = os.path.join(main_folder, subfolder)
        # Get a list of folders in each subfolder
        folders = [folder for folder in os.listdir(subfolder_path) if os.path.isdir(os.path.join(subfolder_path, folder))]
        
        for folder in folders:
            folder_path = os.path.join(subfolder_path, folder)
            # Move the folder and its content back to the main folder
            new_folder_path = os.path.join(main_folder, folder)
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            # Move files from the subfolder to the main folder
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                shutil.move(item_path, new_folder_path)
            # Remove the empty subfolder
            os.rmdir(folder_path)
        
        # Remove the empty subfolder
        os.rmdir(subfolder_path)

# Move folders back to the main folder
move_folders_back()
print("Folders moved back to the main folder.")
