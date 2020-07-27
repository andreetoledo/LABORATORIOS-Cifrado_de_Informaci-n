'''
        Stream Ciphers
        Laboratorio 1

Lehmer random number generator algorithm

Creado por:

    Juan Fernando De Leon Quezada   17822
    Amado Garcia                    181469
    Edgar Andree Toledo             18439
    Ricardo Antonio Valenzuela      18762
    Sara Zavala                     18893

Algorithm

'''

import time

def lehmer(n):
    '''Multiplicative Congruential Generators (Lehmer RNGs)'''

    rng = []

    #a * (m % a) < m

    print("\n\tAsignacion de variables")
    print("\nm = 2**31-1")
    m = 2147483647 #2**31-1
    print("\na = 48271")
    a = 48271
    print("\nq = 44488")
    q = 44488
    print("\nr = 3399")
    r = 3399

    # Set the seed using the current system time in milliseconds.
    print("\n\tSet the seed using the current time in microseconds")
    print("\nSet the seed.")
    millis = int(round(time.time() * 1000))
    # Turn milliseconds to microseconds
    d = millis / 1000
    print("\nCurrent time in milis: ", d)

    print("\n\tInicia operaciones")
    print("\nTal que: r=m mod a and q=m/a")
    for i in range(0, n):
        
        h = d / q
        l = d % q
        t = (a * l) - (r * h)
        
        if t > 0:
            d = t
        else:
            d = t + m
        
        rng.append(round((d / m) * 100))

    return rng