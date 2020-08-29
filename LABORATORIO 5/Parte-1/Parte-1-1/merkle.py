'''
            Lab 5
        Basic Key Exchange
    Implementacion de Merkel's Puzzles

Creado por:
    
    Juan Fernando De Leon Quezada   17822
    Amado Garcia                    181469
    Edgar Andree Toledo             18439
    Ricardo Antonio Valenzuela      18762
    Sara Zavala                     18893

Basado en la implementacion de @heellxz
https://github.com/cvasqxz/merkle/blob/master/merkle.py
'''

from Crypto.Cipher import AES
from random import randint

#private values
s = 25      #len(secret)
N = 100000  #len(secrets)
n = 64      #len(msg)

#Placeholder
msgs = []
keys = []
secrets = []

#ALICE (Encryption)
for i in range(0, N):
    secret = str(randint(1000000000000000000000000, 9999999999999999999999999))
    key = str(randint(1000, 9999))
    key = key*4

    enc_suite = AES.new(key.encode("utf8"), AES.MODE_CBC, key.encode("utf8"))
    msg = '0'*(n-s)
    msg = enc_suite.encrypt(msg.encode("utf8") + secret.encode("utf8"))

    msgs.append(msg)
    keys.append(key)
    secrets.append(secret)

#ALICE sends "msgs" Block to BOB

#BOB (Brute force Decryption)
decrypted_msg = ''
rand_msg_solve = randint(0, N)
msg = '0'*(n-s)

while not decrypted_msg:
    key = str(randint(1000, 9999))
    key = key*4
    dec_suite = AES.new(key.encode("utf8"), AES.MODE_CBC, key.encode("utf8"))
    decrypted_msg = dec_suite.decrypt(msgs[rand_msg_solve])

print('Bob has secret and publishes index')
print('key:', key)
print('index:', rand_msg_solve)

print('Bob decrypted secret:\t', decrypted_msg[(n-s):])
print('Alice secret (' + str(rand_msg_solve) + '):\t' + secrets[rand_msg_solve])