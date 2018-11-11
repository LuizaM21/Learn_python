"""Modul de sincronizare a doua fisere."""
from __future__ import print_function

import sys
import os
import time
import shutil

if len(sys.argv) < 3:
    print("Nu am primit 2 parametri")
    sys.exit(1)

parametru_1 = sys.argv[1]
parametru_2 = sys.argv[2]

# verifcia daca primul parametru este director
if not os.path.isdir(parametru_1):
    print("Primul parametru nu este director ")
    sys.exit(1)

if not os.path.isdir(parametru_2):
    print("Al doilea parametru nu este director ")
    sys.exit(1)

if parametru_1 == parametru_2:
    print("Nu pot sincroniza acelasi director cu el insusi")
    sys.exit(1)

print("Incepem sincronizarea ...")


def get_file(director):
    fisiere_director = []
    for item_name in os.listdir(director):
        full_path = os.path.join(os.path.abspath(director), item_name)
        if os.path.isfile(full_path):
            fisiere_director.append(item_name)
    return fisiere_director


def get_dir(director):
    dirs = []
    for item_name in os.listdir(director):
        full_path = os.path.join(os.path.abspath(director), item_name)
        if os.path.isdir(full_path):
            dirs.append(item_name)
    return dirs


def sincronizeaza_fisiere(sursa, destinatie, prefix=""):
    """Sincronizam directorul sursa cu directorul destinatie."""
    print(prefix, "++ ", sursa, " ... ", destinatie)
    fisiere_sursa = get_file(sursa)
    fisiere_destinatie = get_file(destinatie)

    dirs_sursa = get_dir(sursa)
    dirs_destinatie = get_dir(destinatie)

    print(prefix, "Sursa     : ")
    for item in fisiere_sursa:
        print(prefix, " - {}".format(item))

    print(prefix, "Destinatie: ")
    for item in fisiere_destinatie:
        print(prefix, " - {}".format(item))

    print("\n")
    # sincronizare I - daca un fisier exista in sursa
    #                - dar nu exista in destinatie
    #                ->
    #                * copie fisierul din sursa in destinatie
    for item in fisiere_sursa:
        item_to_copy = os.path.join(os.path.join(sursa, item))
        dest_item = os.path.join(os.path.join(destinatie, item))
        if item not in fisiere_destinatie:
            print(prefix, item_to_copy, " - copy - > ", dest_item)
            shutil.copy(item_to_copy, dest_item)
        else:
            # verific daca continutul difera
            continut_sursa = open(item_to_copy, "r").read()
            continut_destinatie = open(dest_item, "r").read()
            if continut_sursa != continut_destinatie:
                print(prefix, item_to_copy, " - modify - > ", dest_item)
                shutil.copy(item_to_copy, dest_item)

    # sincronizare II - daca un fisier exista in destinatie
    #                 - dar nu exista in sursa
    #                 ->
    #                 * sterge fisierul din destinatie
    for item in fisiere_destinatie:
        if item not in fisiere_sursa:
            item_to_remove = os.path.abspath(os.path.join(destinatie, item))
            print(prefix, item_to_remove, " - remove - > ")
            os.remove(item_to_remove)

    # ----- dirs logic 

    print(prefix, "Dirs Sursa     : ")
    for item in dirs_sursa:
        print(prefix, " - {}".format(item))

    print(prefix, "Dirs Destinatie: ")
    for item in dirs_destinatie:
        print(prefix, " - {}".format(item))

    print("\n")

    for dir_name in dirs_destinatie:
        if dir_name not in dirs_sursa:
            item_to_remove = os.path.join(
                    os.path.abspath(destinatie),
                    dir_name)
            print(prefix, item_to_remove, " - remove dir - >")
            shutil.rmtree(item_to_remove)

    for item in dirs_sursa:
        dir_sursa = os.path.join(os.path.join(sursa, item))
        dir_to_create = os.path.join(os.path.join(destinatie, item))

        if not os.path.exists(dir_to_create):
            os.mkdir(dir_to_create)

        sincronizeaza_fisiere(dir_sursa, dir_to_create, prefix=prefix + "  ")

while True:
    time.sleep(1)
    os.system("clear")
    print("Start sincronizare ...")
    sincronizeaza_fisiere(parametru_1, parametru_2)
