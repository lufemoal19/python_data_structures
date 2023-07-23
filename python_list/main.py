"""
@about python list
@author lufemoal19
@version 0.1
@since 7/22/2023
"""



lista_aplicaciones = [] # 5 aplicaciones

lista_notificaciones = [] # cantidad TOTAL de notificaciones

lista_notificaciones_enviadas = [] # cantidad TOTAL de notificaciones enviadas




def menu():
    print("""\tMENU
[0] SALIR 
[1] CONFIGURACION
[2] PROCESAMIENTO
[3] REPORTES
""")
    opcion = input(str("OPCION: "))
    return opcion

def cargar_datos():
    cantidad = 0
    while cantidad < 5:

        nombre = input(str("NOMBRE DE LA APLICACION: "))
        cantidad_notificaciones = input(int("CANTIDAD TOTAL DE NOTIFICACIONES: "))

        lista_aplicaciones.append(nombre)
        lista_notificaciones.append(cantidad_notificaciones)

        cantidad+=1
    else:
        print("FIN DE LA CONFIGURACION")




if __name__ == "__main__":
    opcion = menu()
    print(f"LA OPCION SELECCIONADA FUE: {opcion}")