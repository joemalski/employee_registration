# Filename: utilities.py
# Date: May 16, 2019
# Description: Contains common modules
# By: Joel F. Malinao

import pathlib as path
import os as os
import ast

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_current_id():
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'id.txt'  

    id_file = open(file_to_open, 'r')
    current_id = id_file.readline()
    id_file.close()
    return int(current_id[12])

def update_current_id(current_id):
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'id.txt'

    id_file = open(file_to_open, 'w')
    current_id = str(current_id + 1)
    current_id = 'current_id: ' + current_id
    id_file.write(current_id)
    id_file.close()

def str_to_dict(str):
    clean_str = str.replace('"', "\"")
    return ast.literal_eval(str)

