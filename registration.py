# Filename: registration.py
# Date: May 17, 2019
# Description: Registration logic.
# By: Joel F. Malinao

import pathlib as path
import modules.utilities as util
import modules.textgui as gui

def init_reg():
    run_entry(util.get_current_id())    

def save_entry(current_id, employee):
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'employee.txt'
    
    emp_file = open(file_to_open, 'a')
    emp_file.write(str(employee)+',')
    emp_file.close()
    util.update_current_id(current_id)
    
    print()
    flag = True
    while flag == True:
        res = input('[A] - Add another Record [X] - Exit Registration: ')
        print('res: ', res)
        if res == 'A' or res == 'a':
            flag = False
            run_entry(util.get_current_id())
        elif res == 'X' or res == 'x':
            flag = False
        else:
            input('Incorrect option selected. Please try again!')


def run_entry(current_id):
    util.clear_screen()
    gui.registration_box()

    employee = {
        'id' : '',
        'first_name' : '',
        'last_name' : '',
        'gender' : '',
        'birthdate' : '',
        'street' : '',
        'city' : '',
        'state' : '',
        'zip_code' : ''
    }

    print()
    print('ID: ', current_id)
    employee['id'] = current_id
    employee['first_name'] = input('Firstname: ')
    employee['last_name'] = input('Lastname: ')
    employee['gender'] = input('Gender: ')
    employee['birthdate'] = input('Birthdate: ')
    employee['street'] = input('Street: ')
    employee['city'] = input('City: ')
    employee['state'] = input('State: ')
    employee['zip_code'] = input('Zipcode: ')
    print()

    flag = True
    while flag == True:
        res = input('Save? [Y/N], Type [C] to Cancel: ')
        if res == 'Y' or res == 'y':
            save_entry(current_id, employee)
            flag = False
        elif res == 'N' or res == 'n':
            run_entry(util.get_current_id())
            flag = False
        elif res == 'C' or res == 'c':
            flag = False
        else:
            input('Incorrect option selected. Please try again!')
