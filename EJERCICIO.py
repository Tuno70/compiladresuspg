def contar_lineas(archivo):
    try:
        with open(archivo, 'r') as archivo_texto:
            contenido = archivo_texto.read()
            num_lineas = contenido.count('\n') + 1
            return num_lineas

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return 0

def contar_palabras(archivo):
    try:
        with open(archivo, 'r') as archivo_texto:
            contenido = archivo_texto.read()
            palabras = contenido.split()
            num_palabras = len(palabras)
            return num_palabras

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return 0

if __name__ == "__main__":
    nombre_archivo = input("Ingrese la ubicación del archivo de texto: ")

    lineas = contar_lineas(nombre_archivo)
    palabras = contar_palabras(nombre_archivo)

    print(f"El número de líneas en el archivo es: {lineas}")
    print(f"El número de palabras en el archivo es: {palabras}")
