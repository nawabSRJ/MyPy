import os

def create_folder(folder_name):
    try:
        # Join the current working directory with the folder name
        folder_path = os.path.join(os.getcwd(), folder_name)
        
        # Create the folder
        os.makedirs(folder_path)
        
        print(f"Folder '{folder_name}' created successfully at {folder_path}")
    except OSError as e:
        print(f"Error creating folder '{folder_name}': {e}")

# Replace 'YourFolderName' with the desired folder name
create_folder('MyFolder2')
