"""
In DevOps, performing regular backups of important files is crucial:
   - Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
   - The script should copy all files from the source directory to the destination directory.
   - Before copying, check if the destination directory already contains a file with the same name. 
     If so, append a timestamp to the file name to ensure uniqueness.
   - Handle errors gracefully, such as when the source directory or destination directory does not exist.
Sample Command:
python backup.py /path/to/source /path/to/destination
By running the script with the appropriate source and destination directories,
it should create backups of the files in the source directory, ensuring unique file names in the destination directory.
"""

import sys
import shutil
import os
from datetime import datetime

def backup_files(source_dir, dest_dir):
    
    #Try block to handle errors gracefully
    try:
        #to check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

        #to check if destination directory exists
        if not os.path.exists(dest_dir):
            print(f"Error: Destination directory '{dest_dir}' does not exist.")
            return

        for file_name in os.listdir(source_dir):
            source_file = os.path.join(source_dir, file_name)
            if os.path.isfile(source_file):
                dest_file = os.path.join(dest_dir, file_name)
                if os.path.exists(dest_file):
                    base, ext = os.path.splitext(file_name)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    new_file_name = f"{base}_{timestamp}{ext}"
                    dest_file = os.path.join(dest_dir, new_file_name)

                # Copy file
                shutil.copy2(source_file, dest_file)
                print(f"Copied: {file_name} -> {dest_file}")

        print("Backup completed successfully!")

    #except blocks to print the errors
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python Regular_Backup.py <source_directory> <destination_directory>")
    else:
        source_dir = sys.argv[1]
        destination_dir = sys.argv[2]
        print("The Source Directory is : ", source_dir)
        print("The Destination Directory is : ", destination_dir)
        backup_files(source_dir, destination_dir)