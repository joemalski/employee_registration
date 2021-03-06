# Filename: main.py
# Date: May 16, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import modules.utilities as util
import modules.textgui as gui
import registration as reg
import searchupdate as search

# selection control
while 1:
    util.clear_screen()
    gui.main_option_box()
    res = input('Select your option: ')

    if res == '1':
        reg.init_registration()
    elif res == '2':
        search.init_search_update()
    elif res == '3':
        print('Bye!')
        break
    else:
        input('Incorrect option selected. Please try again!')

# git hub test 1 push        
