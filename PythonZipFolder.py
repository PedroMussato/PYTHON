# IMPORTING THE REQUIRED LIBRARIES
import zipfile
import os

# CREATING THE FUNCTION THAT PERFORMS THE PROCEDURE
def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, arcname=os.path.relpath(file_path, folder_path))

# DECLARING THE VARIABLES
folder_to_zip = 'folder_path_to_zip'
output_zip_file = 'output_zip_file_path_and_name.zip'

# INVOKING THE FUNCTION
zip_folder(folder_to_zip, output_zip_file)
