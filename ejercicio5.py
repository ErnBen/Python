inicio = 0
limite = 0
print("Programa que importa los numeros pares entre dos numeros dados")
inicio = int(input("Ingrese el valor de inicio"))
limite = int(input("Ahora el valor del fin"))
for x in range(inicio,limite):
 if x % 5 == 0:
   print(f" {x}" , end=" ")
