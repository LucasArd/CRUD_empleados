from Package_Input.Input import *
from elecciones import *

def validar_puesto(puesto: str, mensaje_error: str) -> str:
    while True:
        puesto = puesto.lower()
        match puesto:
            case "gerente" | "supervisor" | "analista" | "encargado" | "asistente":
                break
            case _:
                puesto = input(mensaje_error)
                continue
    return puesto

def calcular_salario_promedio(lista_empleados: list[dict]) -> float:
    suma = 0
    for empleado in lista_empleados:
        suma += float(empleado["salario"])
    promedio = suma / len(lista_empleados)
    return promedio

def match_modificar(opcion, a_modificar):
    match opcion:
        case "A":
            dato = "nombre"
            a_modificar[dato] = get_string("Ingrese el nuevo nombre: ", "El nombre no debe tener mas de 20 caracteres.\nReingrese el nombre: ", 20)
        case "B":
            dato = "apellido"
            a_modificar[dato] = get_string("Ingrese el nuevo apellido: ", "El apellido no debe tener mas de 20 caracteres.\nReingrese el apellido: ", 20)
        case "C":
            dato = "dni"
            a_modificar[dato] = get_int("Ingrese el nuevo DNI: ", "Rango permitido de DNI (50.000.000 - 99.999.999).\nReingrese DNI: ", 50000000, 99999999)
        case "D":
            dato = "puesto"
            a_modificar[dato] = input("Ingrese el nuevo puesto: ")
            puesto = validar_puesto(puesto, f"Error. Ingrese un puesto valido\nOpciones validas: 'Gerente' / 'Supervisor' / 'Analista' / 'Encargado' / 'Asistente'\nPuesto: ")
        case "E":
            dato = "salario"
            a_modificar[dato] = get_min("Ingrese el nuevo salario: $", "El salario minimo es '$234315'\nReingrese el salario: ", 234315)
        case "F":
            return False
        case _:
            print(f"\n{'-'*5}INGRESE UNA OPCION VALIDA{'-'*5}\n")
    return a_modificar

def ordenar_empleados(lista: list[dict]) -> list[dict]:
    opcion = mostrar_menu_ordenar()
    match opcion:
        case "A":
            clave = "nombre"
        case "B":
            clave = "apellido"
        case "C":
            clave = "salario"
        case _:
            print("Error")
    forma = mostrar_menu_ascendente_descendente()
    match forma:
        case "A":
            tipo = False
        case "B":
            tipo = True
        case _:
            print("Error")
    lista_ordenada = sorted(lista, key=lambda x: x[clave], reverse = tipo)
    return lista_ordenada