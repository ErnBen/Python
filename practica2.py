credenciales = {"admin": "12346", "invitado":"root"}

user = input("Ingrese se usario: ")
password = input("Ingrese su contraseña: ")
 
if user in credenciales:
    intentos = 1
    while True:
        if credenciales[user] == password:
            print("Acceso correcto")
            break
        else:
            intentos += 1
            if intentos <= 3:
                password = input(f"Intentos {intentos} de 3. Ingrese su contraseña:")
            else:
                print("Demaciados intentos. Prueben en una hora")
                break
else:
    print("Credenciales invalidos")