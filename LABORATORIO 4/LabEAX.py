# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:10:49 2020
    Ricardo Valenzuela
    Amado Garcia
    Juan Fernando de Leon
    Edgar Toledo
    Sara Zavala

@author: sarit
"""
#References
#https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/#eax-example

from Cryptodome.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2



data= (b'Aqui casual haciendo el lab')
key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_EAX) 
ciphered_data, tag = cipher.encrypt_and_digest(data)

print('Encryptation')
print("Initial enviroment --> ", cipher.nonce)
print('Generated tag --> ', tag)
print('')
print('Encryptade message --> ', ciphered_data)
print('')

nonce = cipher.nonce

print('Decrypting')

cipher = AES.new(key, AES.MODE_EAX, nonce)
original_data = cipher.decrypt_and_verify(ciphered_data, tag) 

print('El mensaje final es: ', original_data)
print('')
if original_data == data:
    print('El mensaje es identico y fue decifrado correctamente')
else:
    print('Error en el proceso de decifrar')