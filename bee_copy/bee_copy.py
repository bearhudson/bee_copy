#!/usr/bin/python3

import os
import shutil
import argparse


def is_subdirectory(parent, child):
    # Check if 'child' is a subdirectory of 'parent'
    return os.path.commonpath([parent, child]) == parent


def copy_images(source_dir, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)
    if is_subdirectory(source_dir, destination_dir):
        print("Error: Destination directory cannot be a subdirectory of the source directory.")
        exit(1)
    # Iterate through all files in the source directory and its subdirectories
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file is an image (you can extend the list of valid extensions)
            image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.JPG', '.JPEG', '.PNG'}
            if any(file.lower().endswith(ext) for ext in image_extensions):
                # Generate the new filename by prefixing the folder name
                folder_name = os.path.basename(root)
                new_filename = f"{folder_name}_{file}"
                # Construct the source and destination paths
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_dir, new_filename)
                # Copy the image file to the destination directory
                shutil.copy2(source_path, destination_path)
    print("Images copied successfully.")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
                        description="A simple utility to copy all images in a source folder to a flat, single folder, "
                                    "renaming the copied files with the source folder's root name.")
    parser.add_argument("-s", "--source", required=True,
                        help="Source directory containing sub-folders to search through.")
    parser.add_argument("-d", "--destination", required=True,
                        help="Destination directory for copied images.")
    args = parser.parse_args()
    # Call the function with the specified source and destination directories
    copy_images(args.source, args.destination)
