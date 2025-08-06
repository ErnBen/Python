texto= input('Introduce un texto: ')
nombre_fichero = 'archivo-' + texto +'.txt'
f = open(nombre_fichero,'w') #apertura w= write, r = read, a = append
mensaje = input("Ingrese un mensaje: ")
f.write(f'{mensaje}\n')
f.close()