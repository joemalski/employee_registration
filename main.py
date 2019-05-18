# Filename: main.py
# Date: May 16, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import modules.utilities as util
import modules.textgui as gui
import registration as reg

# selection control
flag = True
while flag == True:
    util.clear_screen()
    gui.main_option_box()
    select = input('Select your option: ')

    if select == '1':
        reg.init_reg()
    elif select == '2':
        print('option 2 run you modules here!')
        flag = False
    elif select == '3':
        print('option 3 run you modules here!')
        flag = False
    else:
        input('Incorrect option selected. Please try again!')
        