# Filename: searchupdate.py
# Date: May 18, 2019
# Description: Search and Update logic.
# By: Joel F. Malinao

import pathlib as path
import modules.utilities as util
import modules.textgui as gui

def init_search_update():

    # selection control
    flag = True
    while flag == True:
        util.clear_screen()
        gui.search_update_box()
        res = input('Select your option: ')

        if res == '1':
            id = input('Enter ID: ')
            check_id = util.check_emp_id(int(id), True)
            if check_id == False:
                input('ID: '+id+' is NOT Found! Press Enter to try again...')
            else:
                input()
        elif res == '2':
            input('You selected: 2')
        elif res == '3':
            flag = False
        else:
            input('Incorrect option selected. Please try again!')



    '''
    raw_path = path.Path('./flat_files/')
    file_to_open = raw_path / 'employee.txt'
    employee_file = open(file_to_open, 'r+')
    id_found = False
    for employee in employee_file.readlines():
        employee = employee[0:len(employee)-1]
        dict_employee = util.str_to_dict(employee)
        if id == dict_employee['id']:
            print()
            print('ID: ', dict_employee['id'])
            print('Firstname: ', dict_employee['first_name'])
            print('Lastname: ', dict_employee['last_name'])
            print('Gender: ', dict_employee['gender'])
            print('Birthdate: ', dict_employee['birthdate'])
            print('Street: ', dict_employee['street'])
            print('City: ', dict_employee['city'])
            print('State: ', dict_employee['state'])
            print('Zipcode: ', dict_employee['zip_code'])
            id_found = True
            break

    if id_found == False:
        input('ID: '+str(id)+' is not found!, Press enter to continue...')
    else:
        print()
        res = input('Update [U], Delete [D], Cancel [C]: ')
    '''




    
