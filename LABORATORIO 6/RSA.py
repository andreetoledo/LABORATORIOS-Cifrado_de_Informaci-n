#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import math 


class RSA(object):
    def __init__(self):
        '''
            Sets up p, q, n, phi(n) and e values, it also gets the primes from range 2 - 100
        '''
        primes = self._get_primes()
        self.p = random.choice(primes)
        self.q = random.choice([i for i in primes if self.p != i])
        self.n = self.p * self.q 
        self.phi_n = (self.p - 1) * (self.q - 1)
        self.e = random.choice(self.get_coprimes())
    
    def get_coprimes(self):
        '''
            Output: An array of numbers from 1 to Phi(n) where they are coprimes to n and phi(n)
        '''
        coprimes = [i for i in range(1, self.phi_n) if math.gcd(i, self.n) == 1 and math.gcd(i, self.phi_n) == 1]
        return coprimes
    
    def get_public_key(self):
        '''
            Output: A touple representing the public key (n,e)
        '''
        return (self.n, self.e)
    
    def _get_private_key(self):
        '''
            Output: A touple representing the private key (n,e)
        '''
        return (self.n, self._get_d())
        
    def _get_d(self):
        '''
            Output: A random number representing d, chosen from a list of numbers from 1 to e^2
            where each number meets the condition d*e mod phi(n) = 1
        '''
        d_numbers = [d for d in range(1, self.e * self.e) if (d * self.e) % self.phi_n == 1]
        self._d = random.choice(d_numbers)
        return self._d
    
    def _is_prime(self, num):
        '''
            Output: True or false, wheter the number is primer or not
        '''
        for i in range(2,num):
            if (num % i) == 0:
                return False
        return True

    def _get_primes(self):
        '''
            Output: An array of prime numbers from 2 to 100
        '''
        min_prime = 2
        max_prime = 100
        primes = [number for number in range(min_prime,max_prime) if self._is_prime(number)]
        return primes
    
    def cipher(self, text):
        '''
            Input: A plain text that'll be proccessed with the Public key and operated with an equation
            (char ^ public key mod Public Key)
            Output: A ciphered text
        '''
        public_key = self.get_public_key()
        ascii_text = [ord(character) for character in text]
        ciphered_numbers = [(character ** public_key[1]) %  public_key[0] for character in ascii_text]
        ciphered_text = ''.join(chr(i) for i in ciphered_numbers)
        return ciphered_text
    
    def decrypt(self, text):
        '''
            Input: A ciphered text that'll be proccessed with the Private key and operated with an equation
            (char ^ Private key mod Private Key)
            Output: A Plain text
        '''
        private_key = self._get_private_key()
        ascii_text = [ord(character) for character in text]
        decrypted_numbers = [(character ** private_key[1]) %  private_key[0] for character in ascii_text]
        plain_text = ''.join(chr(i) for i in decrypted_numbers)
        return plain_text
    
    def get_data(self):
        '''
            All the important values to be displayed (p, q, n, d, phi(n), e, public key, and private key)
        '''
        return ['p: ' + str(self.p), 
                'q: ' + str(self.q), 
                'n: ' + str(self.n), 
                'd: ' + str(self._get_d()),
                'phi(n): ' + str(self.phi_n), 
                'e: ' + str(self.e),
                'public key: ' + str(self.get_public_key()),
                'private key: ' + str(self._get_private_key())]
    
#==================================================================================================================

rsa = RSA()
text = 'El curso de cifrado es lo máximo'
ciphered_text = rsa.cipher(text)
plain_text = rsa.decrypt(ciphered_text)

print('Texto ingresado: '  + text)
print('Textro cifrado: '   + ciphered_text)
print('Texto descifrado: ' + plain_text)
for data in rsa.get_data():
    print(data)


# In[ ]:




