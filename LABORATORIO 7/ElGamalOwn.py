import random
import math
import hashlib
import bitstring
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class elGamal(object):
    def __init__(self):
        '''
            Sets up q, g, a, h. g is the public key, while a is the private key
        '''
        self.q = random.randint(pow(10, 20), pow(10, 30))
        self.g = random.randint(2, self.q)
        self.a = self.gen_key(self.q)
        self.h = self.exp_mod(self.g, self.a, self.q)

    def GCD(self, a, b):
        '''
            Output: Gets the Greates Comon Divisor between two numbers
        '''
        if a % b == 0:
            return b
        elif a < b:
            return self.GCD(b, a)
        else:
            return self.GCD(b, a % b)

    def gen_key(self, q):
        '''
            Output: Gets a random number in the interval of 10^20 to the length of q. The GCD
            of this number and q has to be 1.
        '''
        key = random.randint(pow(10, 20), q) 
        while self.GCD(q, key) != 1: 
            key = random.randint(pow(10, 20), q)
        return key

    def exp_mod(self, a, b, c):
        '''
            Output: gets the result the power of a number in a given module
        '''
        x = 1
        y = a 
        while b > 0: 
            if b % 2 == 0: 
                x = (x * y) % c
            y = (y * y) % c 
            b = int(b / 2) 
        return x % c

    def cipher(self, text):
        '''
            Input: A plain text
            Output: A ciphered text
        '''
        priv_k = self.gen_key(self.q)
        s = self.exp_mod(self.h, priv_k, self.q) 
        p = self.exp_mod(self.g, priv_k, self.q)

        print('b:', priv_k)
        print('u:', p)
        print('v:', s)
        ascii_text = [ord(character) for character in text]
        ciphered_text = ascii_text
        for i in range(0, len(ascii_text)): 
            ciphered_text[i] = s * ascii_text[i]
        return ciphered_text, p

    def decrypt(self, cipher_text, p):
        '''
            Input: A list with the ciphered representation of characters.
            Output: A Plain text
        '''
        plain_text = ''
        h = self.exp_mod(p, self.a, self.q)
        decrypted_numbers = [int(number/h) for number in cipher_text]
        plain_text = ''.join(chr(i) for i in decrypted_numbers)
        return plain_text
        
    def get_data(self):
        return ['q: ' + str(self.q), 
                'g: ' + str(self.g), 
                'a: ' + str(self.a), 
                'h = g^a: ' + str(self.h)]


gm = elGamal()
for data in gm.get_data():
    print(data)

origin ='Cifrado es chido'
print('Texto original:', origin)
cyphered_nums, p = gm.cipher(origin)
print('Texto cifrado representacion en numeros:', cyphered_nums)
plain_text = gm.decrypt(cyphered_nums, p)
print('Texto descifrado:',plain_text)