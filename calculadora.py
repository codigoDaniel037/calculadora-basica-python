from os import system

def ingreso(dato):
    mensaje = 'Ingrese ' + dato + ' numero: '
    valor = input(mensaje)

    #intentar hacer esto
    try:
        valor = int(valor)
    except:
        #si no se logra realizar la transformacion
        #vamos a generar un error
        valor = 'Error'
    
    if valor == 'Error':
        print('dato erroneo')
        exit()

    return valor 


control = 'y'

while control == 'y':

    system('cls')#limpiar consola o terminal 

    num_1 = ingreso('primer')
    num_2 = ingreso('segundo')

    operacion = input('ingrese la operacion / simbolo ')

    if operacion == '+':
        print('suma: ', num_1 + num_2)
    elif operacion == '-':
        print('resta', num_1 - num_2)
    elif operacion == '*':
        print('multiplicacion', num_1 * num_2)
    elif operacion == '/':
        print('divicion', num_1 / num_2)
    else: 
        print('el simbolo no es valido')

    control = input('quieres hacer una nueva operacion?? y/n ')