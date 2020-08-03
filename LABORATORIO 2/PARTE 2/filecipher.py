import os
from textcipher import TextCipher
  
#THIS FILE CIPHER ONLY WORKS WITH .TXT FILES
#https://nitratine.net/blog/post/encryption-and-decryption-in-python/#generating-a-key-from-a-password
'''
UNIVERSIDAD DEL VALLE DE GUATEMALA
CIFRADO DE INFORMACION
GRUPO: 6 ->
AMADO GARCIA 
SARA ZAVALA
RICARDO VALENZUELA
ANDREE TOLEDO
JUAN FERNANDO DE LEON
'''

#I'm using the encryption and decryption methods from my TextCipher class in the texcipher.py file
#The main difference is that I write out the results in a txt file
class FileCipher(object):

    def __init__(self):
        self.text_cipher = TextCipher()
        self.text = None
    
    #This Method is in charge of encrypting the data that is been read from the file
    #The function takes 3 arguments: The password, the input file name and the output file name (and extensions)
    def encrypt(self, password, input_file, output_file):
        self.text = self.__read(input_file, True)
        if self.text is not None:
            encrypted = self.text_cipher.encrypt(password, self.text.decode())
            self.__write(encrypted, True, output_file)
            return True
        return False
    
    #This Method is in charge of decrypting the data that is been read from the file
    #The function takes 3 arguments: The password, the input file name and the output file name (and extensions)
    def decrypt(self, password, input_file, output_file):
        self.text = self.__read(input_file, False)
        text_dict = {'cipher_text': self.text[0].decode(), 'salt': self.text[1].decode()}
        decrypted = self.text_cipher.decrypt(password, text_dict)
        if decrypted is not None:
            self.__write(decrypted, False, output_file)
            return True
        return False
    
    #Private Method used to write the output (encrypted or decrypted) file. 
    #It takes 3 arguments, the text (encrypted or plain), a boolean indicating wheter it is encrypting or not
    #and the output file name and extension.
    def __write(self, text, isEncrypting, output_file):
        if isEncrypting:
            with open(output_file, 'wb') as f:
                f.write((text['cipher_text'] + "\n").encode())
                f.write(text['salt'].encode())
        else:
             with open(output_file, 'w') as f:
                f.writelines(text)
       
    #Private Method used to read the input (encrypted or decrypted) file. 
    #It takes 2 arguments, a boolean indicating wheter it is encrypting or not
    #and the input file name and extension. It returns the data in the file.
    def __read(self,  input_file, isEncrypting,):
        try:
            if isEncrypting:
                with open(input_file, 'rb') as f:
                    data = f.read()
            else:
                with open(input_file, 'rb') as f:
                    data = f.readlines()
            return data
        except:
            print('This file does not exist')
            
        
'''
i. ¿Qué modo de AES usó? ¿Por qué?
    Referencias: https://stackoverflow.com/questions/1949640/does-iv-work-like-salt
    https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
    Se utilizó PBE (Password Base Encryption) con CBC (Ciphertext Block Chainin), ya que
    se devuelve un iv (salt) y el texto encriptado, cuyos valores se utilizan par desencriptar,
    tal y como se describe en el algoritmo CBC tradicional. Ya que se nos pedía un algoritmo que
    implementara el uso de una contraseña, esté fue el modo utilizado.
    
ii. ¿Qué parámetros tuvo que hacer llegar desde su función de Encrypt a la Decrypt? ¿Por
    1. Password
    2. Input file
    3. Ouput file
    Al igual que en la encriptación de texto, necesitaba saber el Salt y el text encriptado, ya que
    la lógica era la misma, con la diferencia de que el text obtenido se guarda en un archivo .txt.
    La lectura y escritura se raliza en binario.
    
qué?
iii. ¿Qué variables considera las más importantes dentro de su implementación? ¿Por qué?
     1. Password
     2. Input file 
     3. Output file
     4. Text
     Ya que estos son los parámetros pasados en las funciones y que el cipher de texto se encarga del texto,
     lo mas importante era establecer un password, conocer el nombre del archivo a leer, obtener el texto (plano),
     luego el nombre del archivo a escribir y nueva mente el texto (Cifrado) y así el proceso inverso al momento
     de desencriptar.
'''
        