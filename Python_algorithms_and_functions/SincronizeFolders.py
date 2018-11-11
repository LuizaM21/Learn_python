""""
    Synchronize the source folder one with the destination folder.
    If a file is missing from the source folder it will be deleted from the destination folder as well.
    If a file appears in the source folder it will be copied in the destination folder as well
    If a file exists in the destination folder but not in the source folder
    the file will be deleted from the destination folder """

import sys
from os.path import isdir, isfile, join, abspath
from os import listdir, walk
import shutil


# ger directory paths from IDE configuration in -> Run\Edit configurations\Parameters
def get_arguments():
    if len(sys.argv) < 3:
        print("Function does not have 2 parameters")
        sys.exit(1)

    dir_1 = sys.argv[1]
    dir_2 = sys.argv[2]

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


def get_dirs():
    source_dir = get_arguments()[0]
    dir_list = [abspath(join(source_dir, dir_f)) for dir_f in listdir(source_dir) if isdir(join(source_dir, dir_f))]
    # [print("dir_list_item: ", x) for x in dir_list]
    return dir_list


def get_files():
    source_dir = get_arguments()[0]
    file_list = []
    for dir_item, folder_item, file_item in walk(source_dir):
        for f in file_item:
            file_path = join(abspath(dir_item), f)
            file_list.append(file_path)
    return file_list


def get_destination():
    destination_folder = get_arguments()[1]
    return destination_folder


def sync_directory():
    for dirs in get_dirs():
            shutil.copytree(dirs, get_destination())
        #     if os.path.isfile(current_file):
        #         shutil.copy(current_file, destination_f)
        #         return True
        # shutil.copytree(dir_f, destination_f)
    print("Synchronisation is starting!")


if __name__ == '__main__':
    # directly unpack the returned tuple of the function
    # and store them in the function param
    [print("file_item: ", x) for x in get_files()]
    [print("folder_item: ", x)for x in get_dirs()]
    # [print(x) for x in get_arguments()]
    # sync_directory()



