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

import pyotp
import time

#Base 32 OTP
base32secret = 'S3K3TPI5MYA2M67V'
print('Secret:', base32secret)

#Generats OTP based on prev secret
totp = pyotp.TOTP(base32secret)
print('OTP code:', totp.now())

#Wait 30 secs to another Password
print('ESPERA DE 30 SEGS...')
time.sleep(30)
print('OTP code:', totp.now())