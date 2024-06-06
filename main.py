#Alumnos: Astorino Joaquin; Aranda Lucas; Bruzzone Manuel
#Div: 311

from os import system
from Empleado import *

lista = parse_csv_empleados("Empleados.csv")

bandera_ingreso = False
bandera_seguir = True
bandera_limite = False
while bandera_seguir:
    system("cls")
    opcion = mostrar_menu_main()
    #------------------------------------------------------------------------------------------------------
    match opcion:
        case "1":
            bandera_ingreso = True
            if len(lista) < 200:
                id = crear_id('id_lista.txt', lista)
                ingresar_empleado(lista, id)
            else:
                print(f"\n{'-'*3}LIMITE DE EMPLEADOS ALCANZADO{'-'*3}\n")

        #------------------------------------------------------------------------------------------------------
        case "2":
            if bandera_ingreso == True:
                id = get_int("Ingrese el ID a modificar: ", "Error")
                if modificar_empleado(lista, id):
                    print(f"{'-'*3}Modificacion realizada con exito{'-'*3}")
            else:
                print(f"\n{'-'*3}Tiene que agregar al menos 1 empleado para operar{'-'*3}\n")
        #------------------------------------------------------------------------------------------------------
        case "3":

            if bandera_ingreso == False or True:
                id = get_int("Ingrese el ID a eliminar: ", "Error")
                guardar_eliminado(lista, id)
                if eliminar_empleado(lista, id):
                    
                    print(f"{'-'*3}Empleado ({id}) eliminado correctamente{'-'*3}")
            else:
                print(f"\n{'-'*3}Tiene que agregar al menos 1 empleado para operar{'-'*3}\n")
        #------------------------------------------------------------------------------------------------------
        case "4":
            if bandera_ingreso == True:
                print(f"{'*'*54}\n| {'Nombre':>12} | {'Apellido':>12} | {'Puesto':>12} | {'Salario':>12} |\n{'-'*54}")
                mostrar_empleados(lista)
                print(f"{'*'*54}")
            else:
                print(f"\n{'-'*3}Tiene que agregar al menos 1 empleado para operar{'-'*3}\n")
        #------------------------------------------------------------------------------------------------------
        case "5":
            if bandera_ingreso == True:
                promedio = calcular_salario_promedio(lista)
                print(f"\n{'-'*3}Promedio de salarios: {promedio}{'-'*3}\n")
            else:
                print(f"\n{'-'*3}Tiene que agregar al menos 1 empleado para operar{'-'*3}\n")
        #------------------------------------------------------------------------------------------------------
        case "6":
            if bandera_ingreso == True:
                dni = get_int("Ingrese el DNI: ", "Rango permitido de DNI (50.000.000 - 99.999.999).\nReingrese DNI: ", 50000000, 99999999)
                print("Empleado encontrado")
                print(f"{'*'*54}\n| {'Nombre':>12} | {'Apellido':>12} | {'Puesto':>12} | {'Salario':>12} |\n{'-'*54}")
                buscar_por_DNI(lista, dni)
                print(f"{'*'*54}")
            else:
                print(f"\n{'-'*3}Tiene que agregar al menos 1 empleado para operar{'-'*3}\n")
        #------------------------------------------------------------------------------------------------------
        case "7":
            if bandera_ingreso == True:
                lista_ordenada = ordenar_empleados(lista)
                mostrar_empleados(lista_ordenada)
            else:
                print(f"\n{'-'*3}Tiene que agregar al menos 1 empleado para operar{'-'*3}\n")
        #------------------------------------------------------------------------------------------------------
        case "8":
            actualizar_empleados("Empleados.csv", lista)
            bandera_seguir = False
            print(f"\n{'-'*5}Gracias por usar nuestra aplicacion{'-'*5}\n")
        #------------------------------------------------------------------------------------------------------
        case _:
            print(f"\n{'-'*5}INGRESE UNA OPCION VALIDA{'-'*5}\n")
    
    system("pause")
    system("cls")