# Traductor español-inglés usando diccionario

diccionario = {
    "hola": "hello",
    "adios": "goodbye",
    "gracias": "thank you",
    "perro": "dog",
    "gato": "cat"
}

while True:
    palabra = input("Introduce una palabra en español (0 para salir): ").lower()
    
    if palabra == "0":
        print("Traducción finalizada.")
        break

    if palabra in diccionario:
        print(f"La traducción de '{palabra}' es '{diccionario[palabra]}'.")
    else:
        print(f"La palabra '{palabra}' no está en el diccionario.")
        opcion = input("¿Deseas agregarla? (s/n): ").lower()
        if opcion == "s":
            traduccion = input("Introduce la traducción en inglés: ").lower()
            diccionario[palabra] = traduccion
            print(f"Palabra agregada: {palabra} -> {traduccion}")
