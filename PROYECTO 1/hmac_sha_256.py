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

from Crypto.Hash import HMAC, SHA256

from settings import MASTER_KEY

def encrypt(msg):
    '''Encrypt msg with specific key'''
    
    h = HMAC.new(bytes(MASTER_KEY, 'utf-8'), digestmod=SHA256)
    h.update(bytes(msg, 'utf-8'))

    return h.hexdigest()

def verifyMac(h, msg):
    '''Verify if MAC is valid'''
    try:
        h.hexverify(h.hexdigest())
        return "The message '%s' is authentic" % msg
    except ValueError:
        return "The message or the key is wrong"