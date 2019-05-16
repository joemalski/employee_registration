# Filename: utilities.py
# Date: May 16, 2019
# Description: Contains common modules
# By: Joel F. Malinao

import os as os

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
