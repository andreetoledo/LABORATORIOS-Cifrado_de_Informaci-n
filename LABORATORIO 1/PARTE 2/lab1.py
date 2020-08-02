print('--------------------------a--------------------------')
Multiplicador = 915451635481687 
Incremento = 5886893188886454 
Modulo = 6108133789056532 
Cantidadestados = 4
x = 2148910388216139

s4 = ((Multiplicador*x) + Incremento) % Modulo
print('El valor de S4 es:',s4)

print('---------------------------b-------------------------')
Multiplicador = 7544713835650436 
Incremento = 0
Modulo = 3059121001727213 
Cantidadestados = 3
x1 = 1526203935246140
x2 = 1251340539300040 

Incremento = x2 - (Multiplicador*x1) % Modulo
print('El valor del incremento es:',Incremento)
s3 = ((Multiplicador*x2) + Incremento) % Modulo
print('El valor de S3 es:',s3)

print('----------------------------c------------------------')

Multiplicador = 770741127604132 
Incremento = 0
Modulo = 3173287219423490 
Cantidadestados = 3
x1 = 770741127604132
x2 = 2688456964915964
x3 = 2557694464258732

Incremento = x3 - (Multiplicador*x2) % Modulo
print('El valor del incremento es:',Incremento)
s4 = ((Multiplicador*x3) + Incremento) % Modulo
print('El valor de S3 es:',s4)

