""""
    Synchronize the source folder one with the destination folder.
    If a file is missing from the source folder it will be deleted from the destination folder as well.
    If a file appears in the source folder it will be copied in the destination folder as well
    If a file exists in the destination folder but not in the source folder
    the file will be deleted from the destination folder """

import sys
from os.path import isdir, join, abspath
from os import listdir, walk
from inspect import signature
import shutil

input_dir = r"C:\11_synchronize_directories\input_directory"
output_dir = r"C:\11_synchronize_directories\output_directory"


# ger directory paths from IDE configuration in -> Run\Edit configurations\Parameters
def get_arguments(inp_dir, out_dir):
    params = signature(get_arguments)
    params = params.parameters.items()
    if len(params) < 2:
        print("Function does not have 2 parameters")
        sys.exit(1)

    dir_1 = inp_dir
    dir_2 = out_dir

    # verify if first param is a folder director
    if not isdir(dir_1):
        print("First argument is not a valid director!")

    # verify if second param is a folder director
    if not isdir(dir_2):
        print("Second argument is not a valid director!")

    if dir_1 == dir_2:
        print("Cannot synchronize a directory with himself!")
        sys.exit(1)
    return dir_1, dir_2


def get_folders(source_dir):
    dir_list = [dir_f for dir_f in listdir(source_dir) if isdir(join(source_dir, dir_f))]
    return dir_list


def get_files(source_dir):
    file_list = []
    for dir_item, folder_item, file_item in walk(source_dir):
        for f in file_item:
            file_path = join(abspath(dir_item), f)
            file_list.append(file_path)
    return file_list


def sync_directory():
    source_root = get_arguments(input_dir, output_dir)[0]
    source_folders = get_folders(source_root)
    source_files = get_files(source_root)

    destination_root = get_arguments(input_dir, output_dir)[1]
    destination_folders = get_folders(destination_root)
    destination_file = get_files(destination_root)

    [print("source_file: ", item) for item in source_files]
    [print("source_folder: ", item) for item in source_folders]
    [print("destination_file: ", item) for item in destination_file]
    [print("destination_folder: ", item) for item in destination_folders]

    print("Synchronisation is starting!")
    for folder in source_folders:
        if folder not in destination_folders:
            item_to_copy = join(destination_root, folder)
            shutil.copytree(destination_root, item_to_copy)
    print("Synchronisation has finished!")


if __name__ == '__main__':
    # directly unpack the returned tuple of the function
    # and store them in the function param
    # [print("file_item: ", x) for x in get_files(get_arguments()[0])]
    # [print("folder_item: ", x) for x in get_folders(get_arguments()[0])]
    # [print(x) for x in get_arguments()]
    sync_directory()



