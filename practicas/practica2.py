# Diccionario de usuarios y contraseñas
usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "luis": "pass123"
}

usuario = input("Ingrese su nombre de usuario: ")

# Verificar si el usuario existe
if usuario in usuarios:
    intentos = 0
    while intentos < 3:
        contrasena = input("Ingrese su contraseña: ")
        if contrasena == usuarios[usuario]:
            print("Acceso concedido.")
            break
        else:
            intentos += 1
            print(f"Contraseña incorrecta. Intento {intentos}/3.")
    else:
        print("Acceso bloqueado por demasiados intentos fallidos.")
else:
    print("El usuario no existe.")