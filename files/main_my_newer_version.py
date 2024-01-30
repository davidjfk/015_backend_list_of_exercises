__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, zipfile, os.path, re

def main():
    
    # call fn 1of4:
    clean_cache()


    # call fn 2of4:
    # preparation to call fn cache_zip below: 
    # problem: hard coded paths.
    # zipped_file = "C:\dev\pytWinc\wincpy_exercises_and_assignments\files\data.zip"
    # cache_path = "C:\dev\pytWinc\wincpy_exercises_and_assignments\files\cache"


    directory_path = os.getcwd()
    print(f"current working directory: {directory_path}")

    cache_path_unnormalized = (os.path.join(directory_path, "cache")) 
    print(f"cache_path_unnormalized: 1st: {cache_path_unnormalized}")
    cache_path_normalized = os.path.normpath(cache_path_unnormalized)
    print(f"cache_path: {cache_path_normalized}")

    zipped_file_unnormalized = (os.path.join(directory_path, "data.zip")) 
    print(f"path of zipped file: {zipped_file_unnormalized}")
    zipped_file_normalized = os.path.normpath(zipped_file_unnormalized)
    print(f"cache_path: {zipped_file_normalized}")

    cache_zip(zipped_file_normalized, cache_path_normalized)


    # call fn 3of4:
    cached_files_list = cached_files()
    print(cached_files_list)



    # call fn 4of4:
    password_string = find_password(cached_files())
    print(password_string)




def clean_cache():
    # watch out: this fn is deleting files on your computer !!!
    '''
    clean_cache: takes no arguments and creates an empty folder named cache.
    If the folder already exists, it ensures that the folder is empty 
    (so it clears out its contents). 
    '''
    directory_path = os.getcwd()
    '''
    # to run e.g. from terminal: python main.py or 'wincpy check', 
    # you must be in the directory where main.py is located.
    # so you must be in the directory: files. 
    # os.getcwd() returns the current working directory and is always the correct directory,
    # no matter on which machine you run the code.   
    
    '''
    print(f"current working directory: {directory_path}")

    cache_path_unnormalized = (os.path.join(directory_path, "cache")) 
    # pitfall: do not: "\cache" (reason: \c is interpreted as a special character: an escape sequence)
    print(f"cache_path_unnormalized: 1st: {cache_path_unnormalized}")
    #alternative:
    # cache_path_unnormalized = (directory_path + "\cache")
    # print(f"cache_path_unnormalized: {cache_path_unnormalized}")
    # pitfall: do not: "\files\cache" (reason: \f is interpreted as a special character: an escape sequence)

    cache_path = os.path.normpath(cache_path_unnormalized)
    print(f"cache_path: {cache_path}")

    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
        print(f"following directory has been created: {cache_path}")   
        print('-1')   
    else: 
        os.chdir(cache_path)
        if len(os.listdir(cache_path)) != 0:
            [os.remove(f) for f in os.listdir()]
            print(f"result after emptying cache folder: {os.listdir()}")
        else: 
            print('Cache directory is already empty. Nothing to do here.')
    os.chdir(directory_path)







def cache_zip(zip_file_path, cache_dir_path):
    '''
    cache_zip: takes the path to a zip file (str) and the path to a cache directory (str) as arguments.
    Hint: make sure to use this order.
    The function should unpack the zip file into the cache folder that is now clean.

    '''
    # not sure if normalizing is required, because I do not know with what arguments wincpy calls this fn.
    zip_file_path_normalized = os.path.normpath(zip_file_path)
    print(f"zip_file_path: {zip_file_path_normalized}")

    cache_dir_path_normalized = os.path.normpath(cache_dir_path)
    print(f"cache_dir_path: {cache_dir_path_normalized}")

    unzipped_files = zipfile.ZipFile(zip_file_path_normalized, 'r')
    unzipped_files.extractall(cache_dir_path_normalized)
    unzipped_files.close()




def cached_files():
    '''
    takes no arguments and returns a list of all the paths of the files in the cache. 
    These paths should be specified as absolute paths.
    '''

    list_with_absolute_file_names = []
    directory_path = os.getcwd()
    print(f"current working directory: {directory_path}")

    cache_path_unnormalized = (os.path.join(directory_path, "cache")) 
    print(f"cache_path_unnormalized: 1st: {cache_path_unnormalized}")
    cache_path_normalized = os.path.normpath(cache_path_unnormalized)
    print(f"cache_path: {cache_path_normalized}")
     
    # step 1: make list (iterable)  with file names in cache folder
    for file in os.listdir(cache_path_normalized): 
        # step 2: create absolute  path for each file name.
        path_joined_to_file = os.path.join(cache_path_normalized, file)
        # step 3: store each absolute path in a helper var 
        list_with_absolute_file_names.append(path_joined_to_file)    
    return list_with_absolute_file_names







def find_password(list_with_filepaths):
    '''
    takes a list of <absolute /> file paths as an argument. 
    This is the list you got from cached_files.
    This function should read the text in each of the files 
    to see if the password is in there. 

    example text file:
    0.08593691746304766
    0.9234200654025375
    0.6500980385399657
    0.35207903366926374
    0.36798038267970135
    0.7955361681193704
    0.3500762135116595
    0.48800839780286476
    0.7322585972056374
    0.7844841797385017



    Surely there should be a word <look for 'password />
    in there to indicate the presence of the password. Once found, 
    find_password should return this password (str) and nothing else.
    '''
    for file in list_with_filepaths:
        # open each text file in the list:
        file_to_scan_for_password = open(file, "r")
        # read the text in each of the files:
        # note to self: method .read() reads the entire file at once. This could
        # be a problem if the file is very large.
        #2do later: refactor to method .readline() instead.
        file_text = file_to_scan_for_password.read()
        if re.search("password", file_text):
            # (imho) my following lines of code make find_password fn not very generic.
            file_with_password = list(file_text.split("\n"))

            # from here  on I look at one line of code in a text file at a time:
            # refactor (later): use list comprehension to get rid of for loop below.
            for line_of_text_in_file_with_password in file_with_password:
                if re.search("password", line_of_text_in_file_with_password):
                    # easter egg: format appears to be: "password: <password>"
                    password_string_list = list(line_of_text_in_file_with_password.split(":"))
                    password_string = (str(password_string_list[1])).strip()
        # else: 
            # print("password not found in file")
    return password_string


if __name__ == "__main__":

    main()








