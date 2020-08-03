'''
Main Class
UNIVERSIDAD DEL VALLE DE GUATEMALA
CIFRADO DE INFORMACION
GRUPO: 6 ->
AMADO GARCIA 
SARA ZAVALA
RICARDO VALENZUELA
ANDREE TOLEDO
JUAN FERNANDO DE LEON
'''
from textcipher import TextCipher
from filecipher import FileCipher

while(True):
    menu = 'Press 1 To Encrypt and Decrypt a Text\n' + 'Press 2 To Encrypt and Decrypt a .txt File\n' + 'Press anything else to exit\n'
 
    option = input(menu)
    
    if option == '1':
        t_c = TextCipher()

        plain_text = input('Enter the text you want to cypher: ')
        password = input('Enter your password: ')

        encrypted_message = t_c.encrypt(password, plain_text)
        print('Your encrypted messages is: ' + str(encrypted_message) + '\n')

        password = input('Enter your password to decrypt: ')
        decrypted_message = t_c.decrypt(password, encrypted_message)
        print('Your decrypted message is: ' + decrypted_message)

    elif option == '2':
        f_c = FileCipher()  

        pwd = input('Insert your password: ')
        input_file = input('Insert your input filename without the .txt extension')
        output_file = input('Insert your output filename without the .txt extension')
        isValid = f_c.encrypt(pwd, input_file + '.txt', output_file + '.txt')
        if isValid:
            print('Encryption succesful!')
            pwd = input('Insert again your password to decrypt: ')
            isValid = f_c.decrypt(pwd, output_file + '.txt', 'decrypted.txt')
            if isValid:
                print('Decryption succesful, saved on decrypted.txt')
    else:
        print('Good bye')
        break
