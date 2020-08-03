#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode

#CODE REFERENCE: https://nitratine.net/blog/post/encryption-and-decryption-in-python/#generating-a-key-from-a-password
'''
UNIVERSIDAD DEL VALLE DE GUATEMALA
CIFRADO DE INFORMACION
GRUPO: 6 ->
AMADO GARCIA 
SARA ZAVALA
RICARDO VALENZUELA
ANDREE TOLEDO
JUAN FERNANDO DE LEON
'''

#Part 2, exercise 1
class Programa1(object):
    
    #This method returns a tuple, which are the encryption key and the salt value.
    #The function takes 1 argument, the uncoded password written by the user
    def encryption_key(self, password):
        encoded_password = password.encode() #This encodes, to bytes, the password
        salt = os.urandom(16) #Returns a random value of 16 bytes
        kdf = PBKDF2HMAC( #Key derivation Function(algorithm, lenght, salt, iterations, backend)
            algorithm=hashes.SHA256(), 
            length=32,
            salt=salt, #This is a random data that hashes the provided password
            iterations=100000,
            backend=default_backend()
        )
        #This is the resulting key after being proccessed by the kdf and encoded to bytes
        key = base64.urlsafe_b64encode(kdf.derive(encoded_password)) 

        return key, salt
    
     #This method returns the key used to encrypt a text
     #The function takes 2 arguments, the password and the salt.
     #The password must be the same so the key is the same as well
    def decryption_key(self, password, salt):
        encoded_password = password.encode()  #This encodes, to bytes, the password
        salt = b64decode(salt) #Decodes the b64 value of salt to bytes
        kdf = PBKDF2HMAC(       #Key derivation Function(algorithm, lenght, salt, iterations, backend)
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt, #This is a random data that hashes the provided password
            iterations=100000,
            backend=default_backend()
        )
        #This is escencially the same key as the encryption one, if the user provided the same password
        key = base64.urlsafe_b64encode(kdf.derive(encoded_password)) 
        return key
    
    #Encryption function, takes 2 arguments: password and a string
    #Returns a dictionary with a ciphered text and the salt
    def encrypt(self, password, plaintext):
        key, salt = self.encryption_key(password) #calls the encryption_key function to get the key and 
                                                  #salt values

        message = plaintext.encode() #Encodes to bytes the provided message string
        
        #Fernet guarantees that a message encrypted using it can't be manipulated or read without the key.
        f = Fernet(key) 
        
        #This is the encrypted message, using the encrypt function provided by Fernet library
        encrypted = f.encrypt(message)
        return {
        'cipher_text': encrypted.decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        }
         
    #Decryption function, takes 2 arguments: password and a dictionary with keys -> cipher_text and salt
    #Returns a utf-8 type string with the decrypted value
    def decrypt(self, password, encrypted_dict):
        #calls the decryption_key function to get the key used to encrypt the text. Password must match
        key = self.decryption_key(password, encrypted_dict['salt'])
        f = Fernet(key) #Same as described above
        #Fernet provides a decrypt function for encoded text, with the correct key. We also decoded for
        #usability pourposes
        decrypted = f.decrypt(encrypted_dict['cipher_text'].encode()).decode('utf-8')
        return decrypted
    
'''
PREGUNTAS:
i. ¿Tuvo que usar “encode” de algo? ¿Sobre qué variables?
    Sí, usamos encode en varias variables: 
    1) password
    2) key 
    3) El mensaje en texto plano
    4) El mensaje encriptado
    5) La variable Salt (base64)
 
ii. ¿Qué modo de AES usó? ¿Por qué?
Referencias: https://stackoverflow.com/questions/1949640/does-iv-work-like-salt
https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
    Se utilizó PBE (Password Base Encryption) con CBC (Ciphertext Block Chainin), ya que
    se devuelve un iv (salt) y el texto encriptado, cuyos valores se utilizan par desencriptar,
    tal y como se describe en el algoritmo CBC tradicional.

iii. ¿Qué parámetros tuvo que hacer llegar desde su función de Encrypt a la Decrypt? ¿Por qué?
      Devolví desde mi función Encrypt un diccionario con el texto cifrado y el "salt", ya 
      que que salt es generado de forma aleatoria, era necesario mantener el mismo valor para que al hacer
      el hash con el password obtuvieramos la misma key. El texto cifrado lógicamente era necesario para
      poder desencriptarlo.
'''
    

