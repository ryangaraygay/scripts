#!/bin/bash

# Source folder where the files are located
source_folder="/Users/ryangaraygay/Library/MotiveWave/output"  # **CHANGE THIS TO YOUR SOURCE FOLDER**
# Destination folder where the files will be copied
destination_folder="/Users/ryangaraygay/Library/MotiveWave/output/archive"  # **CHANGE THIS TO YOUR DESTINATION FOLDER**

# Check if the source and destination folders exist
if [ ! -d "$source_folder" ]; then
    echo "Source folder '$source_folder' does not exist."
    exit 1
fi

if [ ! -d "$destination_folder" ]; then
    echo "Destination folder '$destination_folder' does not exist."
    exit 1
fi

# Loop through files in the source folder that start with "output"
find "$source_folder" -type f -name "output*" | while IFS= read -r file; do
    # Extract the filename from the full path
    filename=$(basename "$file")
    # Construct the full path for the destination file
    destination_file="$destination_folder/$filename"

    # Check if the file already exists in the destination folder
    if [ ! -e "$destination_file" ]; then
        # Copy the file
        cp "$file" "$destination_file"
        echo "Copied: $filename"
    else
        echo "Skipped: $filename (already exists in destination)"
    fi
done

echo "File copy process complete."
exit 0
