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
            if check_id[0] == False:
                input('ID: '+id+' is NOT Found! Press Enter to try again...')
            else:
                select_edit_option(id, check_id[1])
        elif res == '2':
            input('You selected: 2, Show All Employee')
        elif res == '3':
            flag = False
        else:
            input('Incorrect option selected. Please try again!')


def select_edit_option(id, line_num):
    print()
    flag = True
    while flag == True:
        res = input('[U] - Update, [D] - Delete, [C] - Cancel: ')
        if res == 'U' or res == 'u':
            edit(id, line_num)
            flag=False
        elif res == 'D' or res == 'd':
            input('selected d')
            flag = False
        elif res == 'C' or res == 'c':
            flag = False
        else:
            input('Incorrect option selected. Please try again!')

def edit(id, line_num):

    edit_employee = {
        'id': '',
        'first_name': '',
        'last_name': '',
        'gender': '',
        'birthdate': '',
        'street': '',
        'city': '',
        'state': '',
        'zip_code': ''
    }

    print()
    print('---Update Employee Records---')
    print('ID: ', id)
    edit_employee['id'] = int(id)
    edit_employee['first_name'] = input('Firstname: ')
    edit_employee['last_name'] = input('Lastname: ')
    edit_employee['gender'] = input('Gender: ')
    edit_employee['birthdate'] = input('Birthdate: ')
    edit_employee['street'] = input('Street: ')
    edit_employee['city'] = input('City: ')
    edit_employee['state'] = input('State: ')
    edit_employee['zip_code'] = input('Zipcode: ')

    print()
    flag = True
    while flag == True:
        res = input('Save [Y/N]: ')
        if res == 'Y' or res == 'y':
            util.replace_line(line_num, str(edit_employee)+'\n')
            flag=False
        elif res == 'N' or res == 'n':
            flag = False
        else:
            input('Incorrect option selected. Please try again!')








    
