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
from Crypto.Protocol.KDF import scrypt, PBKDF2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from settings import MASTER_KEY

def key_generation():
    '''Generate PBKDF2 key'''

    # kdf_salt = get_random_bytes(64)
    # key = PBKDF2(MASTER_KEY, kdf_salt)

    # kdf_salt = get_random_bytes(32)
    # key = scrypt(MASTER_KEY, kdf_salt, key_len=32, N=2**17, r=8, p=1)

    salt = get_random_bytes(32)
    #Generado de llave de 32 bytes, se utiliza tando la password como los bytes random
    key = scrypt(MASTER_KEY, salt, key_len=32, N=2**17, r=8, p=1)

    return key

def nonce_generation(key):
    '''Generate Nonce'''
    cipher = AES.new(key, AES.MODE_GCM)
    
    # Nonce is generated randomly if not provided explicitly
    nonce = cipher.nonce

    return nonce

def encrypt(key, plain_text):
    '''Encrypt'''

    # cipher = AES.new(key, AES.MODE_GCM)
    # ciphertext = cipher.encrypt(plain_text)

    # #Encrypt using AES GCM
    # cipher = AES.new(key, AES.MODE_GCM)
    # # Nonce is generated randomly if not provided explicitly
    # nonce = cipher.nonce

    # ciphertext = cipher.encrypt(bytes(plain_text, 'utf-8'))

    #Encryptado
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce

    hoby = bytes(plain_text, 'utf-8')
    encry = cipher.encrypt(hoby)    

    tag = cipher.digest()

    return encry, nonce

def decrypt(encrypted_text, key, nonce):
    '''Decrypt'''

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    decry = cipher.decrypt(encrypted_text)

    # cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    # decrypted_text = cipher.decrypt(encrypted_text)

    return decry.decode('utf-8')

def encrypt_password(password):
    '''Encrypt password'''

    key = key_generation()

    encrypted_password, nonce = encrypt(key, password)

    return encrypted_password, nonce, key

def encrypt_pbkdf2_password(pbkdf2_password, key):
    '''Encrypt PBKDF2 Password'''

    encrypted_password, nonce = encrypt(key, pbkdf2_password)

    return encrypted_password, nonce