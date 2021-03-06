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
    employee_file = open(file_to_open, 'r')

    line_num = 0
    for employee in employee_file.readlines():
        employee = employee[0:len(employee)-1]
        dict_employee = str_to_dict(employee)
        if id == str(dict_employee['id']) and print_option == False:
            employee_file.close()
            return [True, line_num]
        elif id == str(dict_employee['id']) and print_option == True:
            print('----------------------------------------------------')
            print('            E m p l o y e e   F o u n d  !          ')
            print('----------------------------------------------------')
            print('ID:', dict_employee['id'])
            print('Firstname:', dict_employee['first_name'])
            print('Lastname:', dict_employee['last_name'])
            print('Gender:', dict_employee['gender'])
            print('Birthdate:', dict_employee['birthdate'])
            print('Street:', dict_employee['street'])
            print('City:', dict_employee['city'])
            print('State:', dict_employee['state'])
            print('Zipcode:', dict_employee['zip_code'])
            print('----------------------------------------------------')
            employee_file.close()
            return [True, line_num]
        else:
            line_num += 1

    employee_file.close()
    return [False]

def replace_line(line_num, str):
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'employee.txt'
    lines = open(file_to_open, 'r').readlines()
    lines[line_num] = str
    out = open(file_to_open, 'w')
    out.writelines(lines)
    out.close

def show_all_employees():
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'employee.txt'
    employee_file = open(file_to_open, 'r')
    rec_length = 0

    print()
    for employee in employee_file.readlines():
        employee = employee[0:len(employee)-1]
        dict_employee = str_to_dict(employee)
        print('ID: '+str(dict_employee['id'])+'\n'+
            'Name: '+dict_employee['first_name']+' '+dict_employee['last_name']+'\n'+
            'Gender: '+dict_employee['gender']+'\n'+
            'DOB: '+dict_employee['birthdate']+'\n'+
            'Addr: '+dict_employee['street']+' '+dict_employee['city']+' '+dict_employee['state']+' '+
            dict_employee['zip_code']+'\n')
        rec_length = 1

    if rec_length == 1:
        input('Press enter to continue...')
    else:
        input('No records found! Press enter to continue...')





