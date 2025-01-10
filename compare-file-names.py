import os

def get_folder_files(folder_path):
    """Returns a set of file names in the given folder."""
    try:
        return set(os.listdir(folder_path))
    except FileNotFoundError:
        print(f"Error: Folder not found: {folder_path}")
        return set()

def main():
    print("File Comparison Tool")
    folder1 = input("Enter the path for the first folder: ").strip()
    folder2 = input("Enter the path for the second folder: ").strip()

    files1 = get_folder_files(folder1)
    files2 = get_folder_files(folder2)

    common_files = files1.intersection(files2)

    if common_files:
        print("\nFiles existing in both folders:")
        for file in common_files:
            print(file)
    else:
        print("\nNo files are common between the two folders.")

if __name__ == "__main__":
    main()
