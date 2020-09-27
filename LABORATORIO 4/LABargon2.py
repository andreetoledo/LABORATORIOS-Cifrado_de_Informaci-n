# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:51:23 2020

@author:
    Ricardo Valenzuela
    Amado Garcia
    Juan Fernando de Leon
    Edgar Toledo
    Sara Zavala
    
"""
#función para expansión de llaves, Argon2
#Función Hash ( Contraseña ) => Valor Hash
#t - time cost,
#m - memory cost, 
#p - parallelism degree, which defines the number of parallel threads

import argon2
print('')

function = argon2.PasswordHasher()
contrasenia = "Holi que tal"
print('Our password is: ', contrasenia)
print('')
hashed = function.hash(contrasenia)

print(hashed)
print('')
print('$argon2id$ --> The hash is Argon2id, which is the specific Argon2 variant ')
print('$v=19$     --> The version of the hash is 0x13 (19 decimal), meaning Argon2 v1.3')
print('m=102400, t=2, p=8     --> Measures')
print('UhGMbMwITgnuvimAZI/tzg --> The salt ')
print('The password hash itself is: --> YxXkLFsCFYeXwDB0u5QZ0A')

try:
    print('')
    function.verify(hashed, contrasenia)
    print('Verification:', function.verify(hashed, contrasenia))
except argon2.exceptions.VerifyMismatchError:
  print("La verificación con el password `{}` ha fallado".format(contrasenia))
  print('no')

