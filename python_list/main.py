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
[1] CONFIGURACION
[2] PROCESAMIENTO
[3] REPORTES
[0] SALIR 
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

def reporte(cantidad_elementos):
    print("SISTEMA\t\tTOTAL\tENVIADAS\tNO ENVIADAS")
    i = 0
    while i < cantidad_elementos: 
        nombre = lista_aplicaciones[i]
        total = lista_notificaciones[i]
        cantidad_enviadas = lista_notificaciones_enviadas[i]

        print(f"{nombre}\t\t{total}\t{cantidad_enviadas}\t\t\t{total - cantidad_enviadas}")
        i+=1

def programa():
    opcion = 'a'
    cantidad_elementos = 5 # TIENEN QUE SER 5 
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
            reporte(cantidad_elementos)
            pass
        pass
    else:
        print("FIN DEL PROGRAMA")


programa()


# ! -> not  
# == equals ---> equivalente 
# != not equals 
# is --> == 
# is not --> != 