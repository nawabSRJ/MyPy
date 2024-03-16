import os

def check_folder_exists(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    
    if os.path.exists(folder_path):
        print(f"The folder '{folder_name}' exists at {folder_path}")
    else:
        print(f"The folder '{folder_name}' does not exist")

# Replace 'YourFolderName' with the folder name you want to check
check_folder_exists('MyFolder2')
