# -*- coding: utf-8 -*-
"""
Universidad del Valle
Cifrado de Informacion
Laboratorio 7
ElGamal - Library Implementation
Grupo 6

"""

# Referencias:
# https://pythonhosted.org/pycrypto/Crypto.PublicKey.ElGamal-module.html

from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD

'''
Message that we want to encrypt 
'''
message = b"Hello!"
encoding = 'utf-8'

print('El mensaje a cifrar es: ' , message.decode(encoding))

key = ElGamal.generate(1024, Random.new().read)
'''
@ElGamal.generate
Description:
    Randomly generate a fresh, new ElGamal key.
    
Parameters: 
    bits: - Key length, or size (in bits) of the modulus p. 
    
    randfunc: - Random number generation function; it should accept a 
    single integer N and return a string of random data N bytes long.
    
    progress_func=None: - Optional function that will be called with a short 
    string containing the key parameter currently being generated; it's useful 
    for interactive applications where a user is waiting for a key to be generated.

return:
    An ElGamal key object (ElGamalobj).
    
'''

while 1:
    k = random.StrongRandom().randint(1, key.p - 1)
    if GCD(k, key.p - 1) == 1:
        break

h = key.encrypt(message, k)
'''
@Encrypt:
    Encrypt a piece of data with ElGamal.
Parameters:
    plaintext (byte string) - The piece of data to encrypt with ElGamal. 
    It must be numerically smaller than the module (p).
    
    K (long or byte string) - A secret number, chosen randomly in the closed range [1,p-2].

Returns:
    A tuple with two items. Each item is of the same type as the plaintext (string or long).
'''
d = key.decrypt(h)

'''
Parameters:
    ciphertext (byte string, long or a 2-item tuple as returned by encrypt):
        The piece of data to decrypt with ElGamal.
        
Returns:
    A byte string if ciphertext was a byte string or a tuple of byte strings. A long otherwise.
'''

print('El mensaje cifrado es: ', h)
print('El mensaje decifrado es: ', d)