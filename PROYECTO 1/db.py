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
import ast
import uuid
import aes_gcm
import hmac_sha_256
import pbkdf2
from helpers import error_msg, success_msg
from settings import MASTER_KEY

db_path = 'db.txt'
credentials_path = 'credentials.txt'

def read_db():
    '''Read DB from txt file'''

    global db_path

    try:
        #Open txt File
        file = open(db_path, 'r')
        contents = file.read()

        #Turns db into a python dict
        users = ast.literal_eval(contents)

        #Close txt File
        file.close()

        return users
    
    except:
        #In case an error occurs
        print('\nERROR: Ocurrio un problema en la lectura de la base de datos.')

        return {}

def save_db(users):
    '''Save all changes in txt file'''

    global db_path

    try:
        #Abre el archivo
        file = open(db_path, "w")
        file.write(str(users))
        
        #Cierra el archivo txt
        file.close()
        
        success_msg()

        return
    
    except:
        error_msg('ERROR: NO fue posible searizar su transaccion.')

        return

def read_credentials():
    '''Read Credentials from txt file'''

    global credentials_path

    try:
        #Open txt File
        file = open(credentials_path, 'r')
        contents = file.read()

        #Turns db into a python dict
        credentials = ast.literal_eval(contents)

        #Close txt File
        file.close()

        return credentials

    except:
        #In case an error occurs
        print('\nERROR: Ocurrio un problema en la lectura de la base de datos.(Credenciales)')

        return {}

def save_credentials(credentials):
    '''Save Credentials'''

    global credentials_path

    try:
        #Abre el archivo
        file = open(credentials_path, "w")
        file.write(str(credentials))
        
        #Cierra el archivo txt
        file.close()

        return
    
    except:

        return

def user_exists(users, user_name):
    '''Verify if user exists'''

    for user in users.values():
            if (user['user_name'] == user_name):
                return True
    
    return False

def get_user(users, user_name):
    '''Get user'''

    for user in users.values():
            if (user['user_name'] == user_name):
                return user

def get_credentials(credentials, user_id):
    '''Get credentials'''

    for credential in credentials.values():
        if (credential['user_id'] == user_id):
            return credential

def valid_credentials(password, key, nonce, encrypted_password):
    '''Validate credentials'''

    decrypted_password = aes_gcm.decrypt(encrypted_password, key, nonce)

    if (decrypted_password == password):
        return True

    return False
    
def signup_user(user_name, password):
    '''Create a new user'''

    if (user_name and user_name != '' and password and password != ''):
        users = read_db()
        credentials = read_credentials()
        if (users and credentials):
            if (user_exists(users, user_name)):
                error_msg('El nombre de usuario ya existe.')
                return
            else:
                user = {}
                user_credentials = {}
                user_id = str(uuid.uuid4())
                # Hash Password
                encrypted_password, nonce, key = aes_gcm.encrypt_password(password)

                user.update(dict(user_id = user_id, user_name = user_name, password = encrypted_password, accounts = {}))
                user_credentials.update(dict(user_id = user_id, nonce=nonce, key=key))

                users[user_id] = user
                credentials[user_id] = user_credentials

                save_db(users)
                save_credentials(credentials)

                success_msg('Se ha creado su usuario. Inicie Sesion.')

                return

        else:
            error_msg('ERROR: No se encontro ninguna base de datos. Intentelo de nuevo.')
    else:
        error_msg('El nombre de usuario o la contraseña esta en blanco.')

def signin_user(user_name, password):
    '''Login User'''
    if (user_name and user_name != '' and password and password != ''):
        users = read_db()
        credentials = read_credentials()
        if (users and credentials):
            if(user_exists(users, user_name)):
                user = get_user(users, user_name)
                user_credentials = get_credentials(credentials, user['user_id'])

                if (valid_credentials(password, key=user_credentials['key'], nonce=user_credentials['nonce'], encrypted_password=user['password'])):
                    valid = True
                    return valid, user, user_credentials
                else:
                    valid = False
                    return valid, user, user_credentials

            else:
                error_msg('El nombre de usuario no existe.')
                return
        else:
            error_msg('ERROR: No se encontro ninguna base de datos. Intentelo de nuevo.')
    else:
        error_msg('El nombre de usuario o la contraseña esta en blanco.')

def existing_account(accounts, hmac_acct):
    '''Verify if account exist'''

    for account in accounts:
        if (accounts[account]['app'] == hmac_acct):
            return True
    
    return False

def get_existing_account(accounts, hmac_acct):
    '''Returns Account'''

    for account in accounts:
        if (accounts[account]['app'] == hmac_acct):
            return accounts[account]

def save_user(user):
    '''Save user changes'''

    users = read_db()

    if (users):
        
        user_id = user['user_id']

        users[user_id] = user

        save_db(users)

    else:
        error_msg("Ocurrio un error al guardar su informacion. Intentelo de nuevo.")
    
    return user

def new_entry(user, credentials):
    '''Create new entry in db'''

    account = input("\nIngrese su nueva aplicacion: ")

    hmac_acct = hmac_sha_256.encrypt(account)

    # Verify if acct exists allready
    if (existing_account(user['accounts'], hmac_acct)):
        error_msg("La cuenta que desea agregar ya existe.")
    else:
        acct_id = str(uuid.uuid4())
        # Pseudorandom Salt
        salt = pbkdf2._makesalt()
        # PBKDF2 Autogenerated pssword
        pbkdf2_password = pbkdf2.PBKDF2(MASTER_KEY, salt, 1200).hexread(32)

        # AES-GCM Password Encription
        encrypted_pbkdf2_password, nonce = aes_gcm.encrypt_pbkdf2_password(pbkdf2_password, credentials['key'])

        # New Acct Dictionary
        new_acct = {}
        new_acct.update(dict(acct_id=acct_id, app=hmac_acct, password=encrypted_pbkdf2_password, nonce=nonce))

        user['accounts'][acct_id] = new_acct

        user = save_user(user)

        success_msg('Se a guardado su cuenta de la aplicacion {}'.format(account))
    
    return user

def get_entry(user, credentials):
    '''Get User Requested Account'''

    account = input("\nIngrese aplicacion a consultar: ")

    hmac_acct = hmac_sha_256.encrypt(account)

    # Verify if acct exists
    if (existing_account(user['accounts'], hmac_acct)):
        db_account = get_existing_account(user['accounts'], hmac_acct)
        key = credentials['key']
        nonce = db_account['nonce']
        encrypted_password = db_account['password']

        decrypted_password = aes_gcm.decrypt(encrypted_password, key, nonce)

        print("\nAplicacion: ", account)
        print('Password: ', decrypted_password)

        success_msg()
    else:
        error_msg("La cuenta que desea consultar no existe.")

def delete_entry(user, credentials):
    '''Delte Requested entry'''

    account = input("\nIngrese aplicacion a consultar: ")

    hmac_acct = hmac_sha_256.encrypt(account)

    # Verify if acct exists
    if (existing_account(user['accounts'], hmac_acct)):
        acct = get_existing_account(user['accounts'], hmac_acct)
        acct_id = acct['acct_id']
        del user['accounts'][acct_id]

        user = save_user(user) 
        
        success_msg('Se ham guardado sus cambios.')
    else:
        error_msg("La cuenta que desea eliminar no existe.")
    
    return user