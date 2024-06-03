#Alumnos: Astorino Joaquin; Aranda Lucas; Bruzzone Manuel
# Div: 311
def get_int(mensaje: str, mensaje_error: str, minimo: int = None, maximo: int = None, reintentos: int = None) -> int|None:
    while True:
        numero = input(mensaje)
        try:
            numero = int(numero)
            contador = 0
            if minimo != None and maximo != None:
                while numero < minimo or numero > maximo:
                    numero = int(input(mensaje_error))
                    contador += 1
                    if reintentos != None:
                        if contador == reintentos:
                            print("Máximo de reintentos alcanzado")
                            numero = None
                            break
            return numero
        except ValueError:
            print("Error. El numero debe ser entero")


def get_string(mensaje: str, mensaje_error: str, longitud: int = None) -> str|None:
    texto = input(mensaje)
    while True:
        try:
            if longitud != None and len(texto) > longitud and texto.isalpha:
                texto = input(mensaje_error)
                continue
            else:
                return texto
        except ValueError:
            print("Error. Se esperaba una cadena de texto.")


def get_min(mensaje: str, mensaje_error: str, minimo: float = None, reintentos: float = None) -> float|None:
    while True:
        numero = input(mensaje)
        try:
            numero = float(numero)
            contador = 0
            if minimo != None:
                while numero < minimo:
                    numero = float(input(mensaje_error))
                    contador += 1
                    if reintentos != None:
                        if contador == reintentos:
                            print("Máximo de reintentos alcanzado")
                            numero = None
                            break
            return numero
        except ValueError:
            print("Error. El numero debe ser entero")

def get_float(mensaje: str, mensaje_error: str, minimo: float = None, maximo: float = None, reintentos: float = None) -> float|None:
    while True:
        numero = input(mensaje)
        try:
            numero = float(numero)
            contador = 0
            if minimo != None and maximo != None:
                while numero < minimo or numero > maximo:
                    numero = float(input(mensaje_error))
                    contador += 1
                    if reintentos != None:
                        if contador == reintentos:
                            print("Máximo de reintentos alcanzado")
                            numero = None
                            break
            return numero
        except ValueError:
            print("Error. El numero debe ser flotante")


