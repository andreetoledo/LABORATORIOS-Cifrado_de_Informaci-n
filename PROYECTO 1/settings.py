# -*- coding: utf-8 -*-
'''
        Proyecto 1
    Cifrado de Informacion
    Password Manager

Creado por:

    Juan Fernando De Leon Quezada   17822
    Amado Garcia                    181469
    Edgar Andree Toledo             18439
    Ricardo Antonio Valenzuela      18762
    Sara Zavala                     18893

'''
from dotenv import load_dotenv
import os

load_dotenv()

MASTER_KEY = os.getenv("MASTER_KEY")
AAD = os.getenv("AAD")