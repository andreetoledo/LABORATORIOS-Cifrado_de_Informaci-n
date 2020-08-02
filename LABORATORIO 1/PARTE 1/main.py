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

Main

'''

from lehmer import lehmer

if __name__ == '__main__':
    
    rng_results = lehmer(20)

    print("\n\tResultados")
    print("\nSe ejecuto 20 veces el algoritmo.\n")
    i = 1
    for rn in rng_results:
        result = str(i) + ". " + str(rn)
        print(result)
        i += 1
