'''
            Lab 4
        Authenticated Encryption
    Implementacion de GCM
Creado por:
    Juan Fernando De Leon Quezada   17822
    Amado Garcia                    181469
    Edgar Andree Toledo             18439
    Ricardo Antonio Valenzuela      18762
    Sara Zavala                     18893
Basado en
https://nitratine.net/blog/post/python-gcm-encryption-tutorial/
'''
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt

print('---------------------------Implementacion del A.E Galois-Counter Mode (GCM)---------------------------')
# Dato a utilizar para realizar la encriptacion.
password = "password"
# Generando una secuencia de 32 random bytes
salt = get_random_bytes(32)
print('32 Bytes aleatorios:',salt)
#Generado de llave de 32 bytes, se utiliza tando la password como los bytes random
key = scrypt(password, salt, key_len=32, N=2**17, r=8, p=1)
print('Llave:',key)


#input
text = input('Texto a encriptar: ')

#Encryptado
cipher = AES.new(key, AES.MODE_GCM)
nonce = cipher.nonce

hoby = bytes(text, 'utf-8')
encry = cipher.encrypt(hoby)    
print('')
print('Texto cifrado:',encry)

print('')
tag = cipher.digest()
print('Tag:',tag)
print('')

#Desencryptado
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
decry = cipher.decrypt(encry)
print('Texto desencriptado:', decry.decode('utf-8'))