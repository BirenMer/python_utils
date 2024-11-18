import os

def file_path_finder_with_extension(folder_path, file_extensions):
    """
    Finds all files in a folder (and subfolders) with the specified extensions.

    Args:
        folder_path (str): The root directory to search for files.
        file_extensions (list or tuple): The file extensions to look for (e.g., ['.png', '.jpg']).

    Returns:
        list: A list of file paths matching the given extensions.
    """
    # Ensure extensions are in lowercase and form a tuple for faster checks
    file_extensions = tuple(ext.lower() for ext in file_extensions)
    
    all_files_path = []
    for root, _, files in os.walk(folder_path, topdown=True):
        for file in files:
            if file.lower().endswith(file_extensions):
                all_files_path.append(os.path.join(root, file))
    return all_files_path