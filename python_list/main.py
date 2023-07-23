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

def cargar_datos(cantidad_elementos):
    cantidad = 0
    while cantidad < cantidad_elementos:

        nombre = input(str("NOMBRE DE LA APLICACION: "))
        lista_aplicaciones.append(nombre)

        cantidad_notificaciones = input(str("CANTIDAD TOTAL DE NOTIFICACIONES: "))
        lista_notificaciones.append(int(cantidad_notificaciones))

        cantidad+=1
    else:
        print("FIN DE LA CONFIGURACION")

def notificaciones_enviadas(cantidad_notificaciones):
    cantidad_enviada = 0
    cantidad_no_enviada = 0
    for i in range(0, cantidad_notificaciones):
        opcion = input(str("LA NOTIFACION "+ str(i) + " FUE ENVIADA ? [1] SI | [2] NO "))
        if opcion == '1':
            cantidad_enviada+=1
        else:
            cantidad_no_enviada+=1
    return cantidad_enviada


def programa():
    opcion = 'a'
    cantidad_elementos = 2 # TIENEN QUE SER 5 
    while opcion != '0':
        opcion = menu()
        if opcion == '1':
            #CONFIGURACION
            cargar_datos(cantidad_elementos)
            print(f"APLICACIONES: {lista_aplicaciones}")
            print(f"NOTIFICACIONES {lista_notificaciones}")
            pass
        if opcion == '2':
            #PROCESAMIENTO
            # KISP --> KEEP IT STUPID AS POSSIBLE
            
            i = 0
            while i < cantidad_elementos: 
                nombre = lista_aplicaciones[i]
                cantidad = lista_notificaciones[i]
                print(f"APLICACION {nombre} \t TOTAL {cantidad}")
                cantidad_enviadas = notificaciones_enviadas(cantidad)
                lista_notificaciones_enviadas.append(cantidad_enviadas)
                print(f"CANTIDAD NOTIFICACIONES ENVIADAS: {cantidad_enviadas} \n CANTIDAD NOTIFICACIONES NO ENVIADAS: {cantidad - cantidad_enviadas}")
                i+=1
            pass
        if opcion == '3':
            #REPORTE
            print("SISTEMA\tTOTAL\tENVIADAS\tNO ENVIADAS")
            i = 0
            while i < cantidad_elementos: 
                nombre = lista_aplicaciones[i]
                total = lista_notificaciones[i]
                cantidad_enviadas = lista_notificaciones_enviadas[i]

                print(f"{nombre}\t{total}\t{cantidad_enviadas}\t{total - cantidad_enviadas}")
            pass
        pass
    else:
        print("FIN DEL PROGRAMA")


if __name__ == "__main__":
    programa()


# ! -> not  
# == equals ---> equivalente 
# != not equals 
# is --> == 
# is not --> != 