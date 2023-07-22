def es_numero_entero(numero):
    return numero.isdigit()

def es_numero_decimal(numero):
    try:
        float_numero = float(numero)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    numero_ingresado = input("Ingrese un número: ")

    if es_numero_entero(numero_ingresado):
        numero_entero = int(numero_ingresado)
        print(f"El número ingresado es un número entero: {numero_entero}")
    elif es_numero_decimal(numero_ingresado):
        numero_decimal = float(numero_ingresado)
        print(f"El número ingresado es un número decimal: {numero_decimal}")
    else:
        print("El valor ingresado no es un número válido.")
