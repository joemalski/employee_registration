# Filename: main.py
# Date: May 16, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import modules.utilities as util
import modules.textgui as gui
import registration as reg

# selection control
loop_flag = False
while loop_flag == False:
    util.clearScreen()
    gui.mainOptionBox()
    select = input('Select your option: ')

    if select == '1':
        reg.initReg()
    elif select == '2':
        print('option 2 run you modules here!')
        loop_flag = True
    elif select == '3':
        print('option 3 run you modules here!')
        loop_flag = True
    else:
        input('Incorrect option selected. Please try again!')
        