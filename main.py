import os
import sys
import shutil

def split_string_and_get_value_from_index(text_: str, sep_: str, index_: int) -> str:
    """
    Split text_ by separator (sep_) and return the part by index_.
    Example: 
        text_ = filename_1234, sep_ = _, index_ = 1
        output: 1234
    Use this when you want to extract a part of a text asking for an index.
    """
    parts = text_.split(sep_)
    if not isinstance(index_, int):
        raise AssertionError(f"{(type(index_) is int)=}")
    elif not (0 <= index_):
        raise AssertionError(f"{(0 <= index_)=}")
    elif not (index_ < len(parts)):
        raise AssertionError(f"{(index_ < len(parts))=}")
    return parts[index_]

def organize_folder(folderpath: str, sep: str, index: str): 
    """ Organize files in the specified folder by creating subfolders based on extracted indices. 
    
    Steps: 
    1. Take all files from folderpath. 
    2. Extract all indices by name. 
    3. Get unique values. 
    4. For every unique value, create a subfolder named value. 
    5. Put inside the subfolder all files containing value as an index.

    Use this when you want create substructure of a folder path based on rule on file names. 
    """ 
    
    # Step 1: Take all files from folderpath 
    files = [f for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]
    print(f"{files=}")
    # Step 2: Extract all indices by name 
    indices = [split_string_and_get_value_from_index(file, sep, int(index)) for file in files]
    print(f"{indices=}")
    # Step 3: Get unique values 
    unique_indices = set(indices) 

    # Step 4 & 5: For every unique value, create a subfolder named value and move files 
    for i in unique_indices: 
        subfolder_path = os.path.join(folderpath, i) 
        os.makedirs(subfolder_path, exist_ok=True) 
        for file in files: 
            if i == split_string_and_get_value_from_index(file, sep, int(index)): 
                shutil.move(os.path.join(folderpath, file), subfolder_path)

def main(op):
    if op == 0:
        print(split_string_and_get_value_from_index.__doc__)
        text = input("Enter string, separator, and index (e.g., 'filename_1234 _ 1'): \n>")
        values = text.split(" ")
        try:
            output = split_string_and_get_value_from_index(values[0], values[1], int(values[2]))
            print(output)
        except AssertionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    elif op == 1:
        print(organize_folder.__doc__)
        text = input("Enter folderpath, separator, and index (e.g., 'folder/ _ 1'): \n>")
        values = text.split(" ")
        organize_folder(values[0], values[1], values[2])

if __name__ == "__main__":
    op = input("Select operation to perform (e.g., 0 to print docstring and request input): \n>")
    main(int(op))
