#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from base64 import b64encode, b64decode

class Programa1(object):
    def __init__(self):
        pass
    
    def encryption_key(self, password):
        encoded_password = password.encode()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC( #Key derivation Function
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(encoded_password))
        return key, salt
    
    def decryption_key(self, password, salt):
        encoded_password = password.encode()
        salt = b64decode(salt)
        kdf = PBKDF2HMAC( #Key derivation Function
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(encoded_password))
        return key
    
    def encrypt(self, password, plaintext):
        key, salt = self.encryption_key(password)

        message = plaintext.encode()
        f = Fernet(key)
        encrypted = f.encrypt(message)
        return {
        'cipher_text': encrypted.decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        }
         
    def decrypt(self, password, encrypted_dict):
        key = self.decryption_key(password, encrypted_dict['salt'])
        f = Fernet(key)
        decrypted = f.decrypt(encrypted_dict['cipher_text'].encode()).decode('utf-8')
        return decrypted
    

