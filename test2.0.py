from urllib import request
from urllib.error import URLError

# Lista de palabras ofensivas
palabras_ofensivas = ["coño", "bobo", "culiao", "pinche", "estupido", "estupida"]

def verificar_web(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return f'¡La URL "{url}" no existe!'
    else:
        contenido = f.read().decode('utf-8').lower()  # decodificamos y pasamos a minúsculas
        palabras_encontradas = []

        for palabra in palabras_ofensivas:
            if palabra in contenido:
                palabras_encontradas.append(palabra)
        
        return palabras_encontradas

def notificar_si_hay_ofensivas(palabras_encontradas, url):
    if palabras_encontradas:
        print("\n-------------------------------------------")
        print("¡Atención! Se encontraron palabras ofensivas en el sitio:")
        print(f"URL: {url}")
        print(f"Palabras encontradas: {', '.join(palabras_encontradas)}")
        print("-------------------------------------------\n")
    else:
        print("\n-------------------------------------------")
        print("No se encontraron palabras ofensivas en el sitio.")
        print("-------------------------------------------\n")

# URL a analizar
url = 'https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'

print("\nAnalizando sitio:", url)

# Ejecutar análisis
palabras_encontradas = verificar_web(url)

# Notificar resultado
notificar_si_hay_ofensivas(palabras_encontradas, url)

