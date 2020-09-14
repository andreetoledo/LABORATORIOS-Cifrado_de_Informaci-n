# -*- coding: utf-8 -*-
'''
        Proyecto 1
    Cifrado de Informacion
    Password Manager

Creado por:

    Juan Fernando De Leon Quezada   17822
    Amado Garcia                    181469
    Edgar Andree Toledo             18439
    Ricardo Antonio Valenzuela      18762
    Sara Zavala                     18893

'''
# import only system from os 
from os import system, name 

import getpass

def valid_menu_input(op):
    '''Verify if input is a Integer'''
    try:
        op = int(op)
        return True
    except:
        return False

def clear(): 
    '''Clear Screen'''
    
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def error_msg(msg = None):
    '''Hanlde Error Msgs'''

    if msg:
        error_msg = '\nERROR: {}'.format(msg)
        print(error_msg)
    else:
        print('\nERROR: Ocurrio un error. Intentelo de nuevo.')
    input('\nPresiones la tecla ENTER para continuar...')

def success_msg(msg = None):
    '''Hanlde Success Msgs'''

    if msg:
        success_msg = '\nEXITO: {}'.format(msg)
        print(success_msg)
    else:
        print('\nEXITO: Su transaccion fue realizada.')
    input('\nPresiones la tecla ENTER para continuar...')

def input_password():
    '''Read password'''
    try:
        password = getpass.getpass()
        return password
    except:
        error_msg("ERROR: Ocurrio un problema al leer la contraseña. Intentelo denuevo.")
        return
    