__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

def main():
    
    clean_cache()

    zipped_file = "C:/dev/pytWinc/list_python_assignments/files/data.zip"
    cache_dir_path = "C:/dev/pytWinc/list_python_assignments/files/cache"
    cache_zip(zipped_file, cache_dir_path)

    cached_files_list = cached_files()
    print(cached_files_list)

    password_string = find_password(cached_files())
    print(password_string)



import os
def clean_cache():
    directory_path = os.getcwd()
    cache_path_unnormalized = (os.path.join(directory_path, "files\cache"))
    cache_path = os.path.normpath(cache_path_unnormalized)

    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
        print(f"following directory has been created: {cache_path}")       
    else: 
        os.chdir(cache_path)
        if len(os.listdir(cache_path)) != 0:
            [os.remove(f) for f in os.listdir()]
            print(f"result after emptying cache folder: {os.listdir()}")
        else: 
            print('hi there')
    os.chdir(directory_path)


import zipfile
def cache_zip(zip_file_path, cache_dir_path):
    unzipped_files = zipfile.ZipFile(zip_file_path, 'r')
    unzipped_files.extractall(cache_dir_path)


import os.path
def cached_files():
    list_with_absolute_file_names = []
    directory_path = os.getcwd()
    cache_path_unnormalized = (os.path.join(directory_path, "files\cache"))
    cache_path = os.path.normpath(cache_path_unnormalized)
     
    for file in os.listdir(cache_path):        
        path_plus_file = os.path.join(cache_path, file)
        list_with_absolute_file_names.append(path_plus_file)    
    return list_with_absolute_file_names

import re
def find_password(list_with_filepaths):
    for file in list_with_filepaths:
        file_to_scan_for_password = open(file, "r")
        file_text = file_to_scan_for_password.read()
        if re.search("password", file_text):
            # (imho) my following lines of code make find_password fn not very generic.
            file_with_password = list(file_text.split("\n"))
            for list_item_with_password in file_with_password:
                if re.search("password", list_item_with_password):
                    password_string_list = list(list_item_with_password.split(":"))
                    password_string = (str(password_string_list[1])).strip()
    return password_string


if __name__ == "__main__":

    main()








