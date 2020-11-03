'''

        Laboratorio 9
    One Time Password



Creado por:

    Juan Fernando De Leon Quezada   17822
    Amado Garcia                    181469
    Edgar Andree Toledo             18439
    Ricardo Antonio Valenzuela      18762
    Sara Zavala                     18893

Basado en:

https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/more-cryptographic-concepts/one-time-passwords-otp-example.html

'''

import scrypt

#Message
msg = 'Alice y bob.'
print('\nMsg: ', msg)
#Password
password = 'CC3078CCTI'

encryptedMsg = scrypt.encrypt(msg, password, maxtime=0.1) # This will take at least 0.1 seconds

#se mostrata el mensaje
print('\nEste es el mensaje cifrado', encryptedMsg)

#aqui mostraremos el mensaje recibido y sera descenriptado
#esta funcion recibe como parametros el mensaje, la llave y el tiempo
decryptedMsg = scrypt.decrypt(encryptedMsg, password, maxtime=0.1)
print('\nEl mensaje recibido es: ', decryptedMsg)