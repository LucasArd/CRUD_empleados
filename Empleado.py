
from funciones import *
import json


#region Create
def crear_empleado(id: int, dni: int, nombre: str, apellido: str, puesto: str, salario: float) -> dict:
    diccionario_empleados = {
        "ID": id,
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "puesto": puesto,
        "salario": salario
    }
    return diccionario_empleados

def ingresar_empleado(lista_empleados: list, id: int) -> bool: #Mejorar y validar
    dni = get_int("Ingrese el DNI: ", "Rango permitido de DNI (50.000.000 - 99.999.999).\nReingrese DNI: ", 50000000, 99999999)
    nombre = get_string("Ingrese el nombre: ", "El nombre debe ser alfabetico y no debe tener mas de 20 caracteres.\nReingrese el nombre: ", 20)
    apellido = get_string("Ingrese el apellido: ", "El apellido debe ser alfabetico y no debe tener mas de 20 caracteres.\nReingrese el apellido: ", 20)
    puesto = input("Ingrese el puesto: ")
    puesto = validar_puesto(puesto, f"Error. Ingrese un puesto valido\nOpciones validas: 'Gerente' / 'Supervisor' / 'Analista' / 'Encargado' / 'Asistente'\nPuesto: ")
    salario = get_min("Ingrese el salario: $", "El salario minimo es '$234315'\nReingrese el salario: ", 234315)

    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    puesto = puesto.capitalize()

    diccionario_empleados = crear_empleado(id, dni, nombre, apellido, puesto, salario)
    lista_empleados.append(diccionario_empleados)
    salida = True
    return salida
#endregion


#region Read
def mostrar_un_empleado(empleado: dict): #Mejorar
    print(f"| {empleado['nombre']:>12} | {empleado['apellido']:>12} | {empleado['puesto']:>12} | {empleado['salario']:>12} |\n")

def mostrar_empleados(lista_empleados: list[dict]): #Mejorar
    for empleado in lista_empleados:
        mostrar_un_empleado(empleado)
#endregion


#region Update
def buscar_por_DNI(lista_empleados: list[dict], dni: int):
    for empleado in lista_empleados:
        if dni == empleado["dni"]:
            busqueda = empleado
            mostrar_un_empleado(busqueda)

def modificar_empleado(lista_empleados: list[dict], id: int) -> bool:
    try:
        salida = False
        for empleado in lista_empleados:
            if id == empleado["ID"]:
                a_modificar = empleado
                print("Empleado encontrado")
                while True:
                    opcion = mostrar_menu_modificar()
                    if not match_modificar(opcion, a_modificar):
                        break
                salida = True
                break
        return salida
    except UnboundLocalError:
        print("Ese ID no existe (quizas fue borrado)")
#endregion


#region Delete
def eliminar_empleado(lista_empleados: list[dict], id: int) -> bool:
    try:
        eliminar = None
        for empleado in lista_empleados:
            if id == empleado["ID"]:
                print("Empleado encontrado")
                eliminar = empleado
                break
        if eliminar != None:
            lista_empleados.remove(eliminar)
            print(lista_empleados)
            salida = True
        return salida
    except UnboundLocalError:
        print("Ese ID no existe (quizas fue borrado)")
#endregion