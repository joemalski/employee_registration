# Filename: utilities.py
# Date: May 16, 2019
# Description: Contains common modules
# By: Joel F. Malinao

import pathlib as path
import os
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

def check_emp_id(id, print_option):
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'employee.txt'
    employee_file = open(file_to_open, 'r+')

    for employee in employee_file.readlines():
        employee = employee[0:len(employee)-1]
        dict_employee = str_to_dict(employee)
        if id == dict_employee['id'] and print_option == False:
            return True
        elif id == dict_employee['id'] and print_option == True:
            print('----------------------------------------------------')
            print('            E m p l o y e e   F o u n d  !          ')
            print('----------------------------------------------------')
            print('ID: ', dict_employee['id'])
            print('Firstname: ', dict_employee['first_name'])
            print('Lastname: ', dict_employee['last_name'])
            print('Gender: ', dict_employee['gender'])
            print('Birthdate: ', dict_employee['birthdate'])
            print('Street: ', dict_employee['street'])
            print('City: ', dict_employee['city'])
            print('State: ', dict_employee['state'])
            print('Zipcode: ', dict_employee['zip_code'])
            print('----------------------------------------------------')
            return True
    return False





