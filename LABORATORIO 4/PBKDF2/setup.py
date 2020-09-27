#Laboratorio 4 Cifrado

#    : copyright: (c) Copyright 2011 de Armin Ronacher.
#   : licencia: BSD, consulte LICENCIA para obtener más detalles.
# -*- coding: utf-8 -*-

"""
  Este módulo implementa pbkdf2 para Python. También tiene algunos básicos
    pruebas que aseguran que funciona. La implementación es sencilla
    y usa solo cosas de stdlib y se puede copiar / pegar fácilmente en
    tu aplicación favorita.

    Use esto como reemplazo de bcrypt que no necesita una implementación de c
    de un algoritmo criptográfico de pez globo modificado.

    Uso de ejemplo:

    >>> pbkdf2_hex ('lo que quiero hash', 'la sal aleatoria')
    'fa7cc8a2b0a932f8e6ea42f9787e9d36e592e0c222ada6a9'

    Como usar esto:

    1. Utilice una función de comparación de cadenas de tiempo constante para comparar el hash almacenado
        con el que estás generando:

            def safe_str_cmp (a, b):
                si len (a)! = len (b):
                    falso retorno
                rv = 0
                para x, y en izip (a, b):
                    rv | = ord (x) ^ ord (y)
                return rv == 0

    2. Utilice `os.urandom` para generar una sal adecuada de al menos 8 bytes.
        Utilice una sal única por contraseña hash.

    3. Almacene el `` algoritmo $ salt: costfactor $ hash '' en la base de datos para que
        puede actualizar más tarde fácilmente a un algoritmo diferente si lo necesita
        uno. Por ejemplo, `` PBKDF2-256 $ thesalt: 10000 $ deadbeef ... ''.



"""
try:
    from setuptools import setup
except ImportError:
    import sys
    sys.stderr.write("warning: Proceeding without setuptools\n")
    from distutils.core import setup

from pbkdf2 import __version__

setup(
    name='pbkdf2',
    py_modules=['pbkdf2'],
    version=__version__,
    test_suite='test',
    description='PKCS#5 v2.0 PBKDF2 Module',
    author='Dwayne C. Litzenberger',
    author_email='dlitz@dlitz.net',
    url='http://www.dlitz.net/software/python-pbkdf2/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
    ],
    long_description="""\
This module implements the password-based key derivation function, PBKDF2, specified in RSA PKCS#5 v2.0.
""")
