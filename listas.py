import re

def separar_palabras_numeros_signos(texto):
    
    patron_palabras = r'\b[a-zA-Z]+\b'

    
    patron_numeros = r'[-+]?\d*\.\d+|\d+'

    
    patron_signos = r'[^\w\s]'

    
    palabras = re.findall(patron_palabras, texto)
    numeros = re.findall(patron_numeros, texto)
    signos = re.findall(patron_signos, texto)

    return palabras, numeros, signos

if __name__ == "__main__":
    nombre_archivo = input("Ingrese la ubicación del archivo de texto: ")

    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras, numeros, signos = separar_palabras_numeros_signos(contenido)

            print("Palabras:", palabras)
            print("Números:", numeros)
            print("Signos:", signos)

    except FileNotFoundError:
        print("El archivo no fue encontrado.")

