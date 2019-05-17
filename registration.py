# Filename: registration.py
# Date: May 17, 2019
# Description: Registration logic.
# By: Joel F. Malinao

import pathlib as path
import modules.utilities as util
import modules.textgui as gui

def initReg():
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'id.txt'
    
    id_file = open(file_to_open, 'r')
    current_id = id_file.readline()
    runEntry(current_id[12])
    id_file.close()

def writeEntry(current_id, employee):
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'employee.txt'
    
    emp_file = open(file_to_open, 'a')
    emp_file.write(str(employee)+',')
    emp_file.close()

def runEntry(current_id):
    util.clearScreen()
    gui.registrationBox()

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
        res = input('Save? Y/N, Type C to cancel: ')
        if res == 'Y' or res == 'y':
            print('save')
            writeEntry(current_id, employee)
            flag = False
        elif res == 'N' or res == 'n':
            runEntry(current_id)
            flag = False
        elif res == 'C' or res == 'c':
            flag = False
