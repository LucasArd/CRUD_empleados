from Package_Input.Input import *

def mostrar_menu_ordenar() -> str:
    opcion = input(f"{'-'*5}Ordenar por:{'-'*5}\nA) Nombre\nB) Apellido\nC) Salario\n{'-'*5}\nSu eleccion: ")
    opcion = opcion.upper()
    return opcion

def mostrar_menu_ascendente_descendente() -> str:
    opcion = input(f"{'-'*5}Ordenar de forma:{'-'*5}\nA) Ascendente\nB) Desdendente\n{'-'*5}\nSu eleccion: ")
    opcion = opcion.upper()
    return opcion

def mostrar_menu_modificar() -> str:
    opcion = input(f"{'-'*5}¿Que desea modificar?{'-'*5}\nA) Nombre\nB) Apellido\nC) DNI\nD) Puesto\nE) Salario\nF) Salir\n{'-'*5}\nSu eleccion: ")
    opcion = opcion.upper()
    return opcion

def mostrar_menu_main() -> int:
    eleccion = (input(f"{'-'*5}Menu de opciones{'-'*5}\n1) Ingresar empleado\n2) Modificar empleado\n3) Eliminar empleado\n4) Mostrar todos\n5) Calcular salario promedio\n6) Buscar empleados por DNI\n7) Ordenar empleados\n8) Salir\n{'-'*5}\nSu eleccion: "))
    return eleccion

