'''
            Lab 3
        Message Integrity

    Implementacion de HMAC-SHA-256

Creado por:
    
    Juan Fernando De Leon Quezada   17822
    Amado Garcia                    181469
    Edgar Andree Toledo             18439
    Ricardo Antonio Valenzuela      18762
    Sara Zavala                     18893

Basado en la implementacion de PyCryptodome

https://pycryptodome.readthedocs.io/en/latest/src/hash/hmac.html

'''

from Crypto.Hash import HMAC, SHA256

def encrypt(key, msg):
    '''Encrypt msg with specific key'''
    
    h = HMAC.new(key, digestmod=SHA256)
    h.update(msg)

    return h

def verifyMac(h, msg):
    '''Verify if MAC is valid'''
    try:
        h.hexverify(h.hexdigest())
        return "The message '%s' is authentic" % msg
    except ValueError:
        return "The message or the key is wrong"

print('\n\t\tLab 3\n\tMessage Integrity')

print('\n1.\n\ta) Key: CC3078 Msg: Cifrado de informacion seccion 10')

k1 = b'CC3078'
msg1 = b'Cifrado de informacion seccion 10'

h = encrypt(k1, msg1)

print('\n\t\tEncrypted: ', h.hexdigest())

print("\t\t", verifyMac(h, msg1))

print('\n2.\n\tb) Key: MAC Msg: La implementacion de este ejercicio fue sencilla')

k2 = b'MAC'
msg2 = b'La implementacion de este ejercicio fue sencilla'

h2 = encrypt(k2, msg2)

print('\n\t\tEncrypted: ', h2.hexdigest())

print("\t\t", verifyMac(h2, msg2))

'''
try:
    h.hexverify(mac)
    print("The message '%s' is authentic" % msg)
except ValueError:
    print("The message or the key is wrong")
'''