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

from helpers import *
from db import signup_user, signin_user, new_entry, get_entry, delete_entry

def main_menu():
    '''Main Menu'''
    return '''
    
    \tPassword Manager

    1. Iniciar Sesion
    2. Crear un Usuario
    3. Salir

    '''

def user_menu():
    '''User Menu'''

    return '''
    
    \tMenu Principal

    1. Crear un nuevo registro
    2. Mostrar un registro
    3. Eliminar un registro
    4. Salir

    '''

if __name__ == '__main__':
    '''Main Program'''

    clear()

    wants_to_continue = True

    while (wants_to_continue):
        '''Main Menu'''
        
        clear()

        #Print Main Menu
        print(main_menu())

        #Input Menu Option
        op = input('Ingrese una opcion: ')
        clear()

        #Verify Menu Options
        if (valid_menu_input(op)):
            if (op == '1'):
                # Inicia Sesion
                print("\n\tIniciar Sesion")
                user_name = input("\nIngrese su nombre de usuario:")
                password = input_password()

                if (password):
                    valid_credentials, user, user_credentials = signin_user(user_name, password)
                    if (valid_credentials):
                        wants_to_continue_user_menu = True

                        while wants_to_continue_user_menu:
                            '''Main User Menu'''

                            clear()

                            # Print User Menu
                            print(user_menu())

                            #Input Menu Option
                            op = input('Ingrese una opcion: ')
                            clear()

                            if (valid_menu_input(op)):
                                if (op == '1'):
                                    print("\n\tCrear un nuevo registro")
                                    user = new_entry(user, user_credentials)
                                elif (op == '2'):
                                    print("\n\tMostrar un registro")
                                    get_entry(user, user_credentials)
                                elif (op == '3'):
                                    print("\n\tEliminar un registro")
                                    user = delete_entry(user, user_credentials)
                                elif (op == '4'):
                                    wants_to_continue_user_menu = False
                                else:
                                    error_msg('La opcion ingresada no es valida.')
                            else:
                                error_msg('La opcion ingresada no es valida.')

                    else:
                        error_msg("Las credenciales son invalidas.")
            elif (op == '2'):
                # Crear Usuario
                print("\n\tCrear un Usuario")
                user_name = input("\nIngrese su nombre de usuario:")
                password = input_password()

                if (password):
                    signup_user(user_name, password)

                print('hola 2')
            elif (op == '3'):
                # Salir
                wants_to_continue = False
            else:
                error_msg('La opcion ingresada no es valida.')
        else:
            error_msg('La opcion ingresada no es valida.')