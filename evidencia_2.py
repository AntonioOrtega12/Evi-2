# Modulos

import datetime
import csv
import os

# Diccionarios

clientes_dict = dict()
salas_dict = dict()
reservas_dict = dict()
turno_dict = {1: "Matutino", 2: "Vespertino", 3: "Nocturno"}

if os.path.isfile("clientes.csv") and os.path.isfile("salas.csv") and os.path.isfile("reservas.csv"):

    with open("clientes.csv","r", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        
        for clave, nombre in lector:
            clientes_dict[int(clave)] = nombre

    with open("salas.csv","r", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        
        for clave, nombre, cupo in lector:
            salas_dict[int(clave)] = (nombre, int(cupo))

    with open("reservas.csv","r", newline="") as archivo:
        lector = csv.reader(archivo)
        next(lector)
        
        for folio, fecha, sala, cliente, evento, turno in lector:
            salas_dict[int(folio)] = (fecha, int(sala), cliente, evento, turno)
else:
    print("\nEs la primera vez que se ejecuta el programa.")
while True:

    print("""
    --------------------------------MENU PRINCIPAL--------------------------------\n
    [A] RESERVACIONES.\n
    [B]	REPORTES\n
    [C]	REGISTRAR NUEVO CLIENTE.\n
    [D]	REGISTRAR NUEVA SALA.\n
    [E] Salir
    """)

    opcion_menu = input("\nSeleccione una opcion: ")

    if opcion_menu.upper() == "A":
        while True:

            print("""
    --------------------------------MENU RESERVAS--------------------------------\n
    [A] REGISTRAR NUEVA RESERVACION\n
    [B]	MODIFICAR DESCRIPCION DE UNA RESERVACIÓN\n
    [C]	CONSULTAR DISPONIBIBLIDAD DE SALAS PARA UNA FECHA\n
    [D]	VOLVER AL MENU PRINCIPAL\n
    """)

            opcion_menu_reservas = input("Elija una opcion: ")

            if opcion_menu_reservas.upper() == "A":
                print(f"\n{'Clientes registrados':^40}")
                print("-" * 40)
                print("Clave\t\tCliente")
                print("-" * 40)
                for clave, nombre in clientes_dict.items():
                    print(f"{clave}\t\t{nombre}")
                print("-" * 40)
                while True:

                    clave_de_cliente_reserva_capturada = input("\nEscribe su clave del cliente: ")

                    if clave_de_cliente_reserva_capturada.strip() == "":
                        print("\nNo puede omitirse.")
                        continue

                    try:
                        clave_de_cliente_reserva = int(clave_de_cliente_reserva_capturada)
                    except Exception:
                        print("\nNo es de tipo entero.")
                        continue

                    if clave_de_cliente_reserva in clientes_dict:
                        print(f"\nCliente {clientes_dict[clave_de_cliente_reserva]} puede hacer la reservacion.")
                        break
                    else:
                        print("Clave cliente no existe.")
                        continue

                while True:
                    clave_de_sala_reservas_capturada = input("\nEscriba el numero de sala: ")

                    if clave_de_cliente_reserva_capturada.strip() == "":
                        print("\nNo puede omitirse.")
                        continue

                    try:
                        clave_de_sala_reservas = int(clave_de_sala_reservas_capturada)
                    except Exception:
                        print("\nNo es de tipo entero.")

                    if clave_de_sala_reservas in salas_dict:
                        print(f"\nSala {clave_de_sala_reservas} seleccionada.")
                        break
                    else:
                        print("\nClave de sala no existe.")
                        continue

                while True:

                    fecha_actual = datetime.date.today()

                    fecha_reservacion_capturada = input("\nEscribe la fecha de reservacion que desea con el formato dd/mm/aaaa: ")

                    if fecha_reservacion_capturada.strip() == "":
                        print("\nNo puede omitirse.")
                        continue

                    try:
                        fecha_reservacion = datetime.datetime.strptime(fecha_reservacion_capturada, "%d/%m/%Y").date()
                    except Exception:
                        print("\nFormato de fecha no correcto.")
                        continue

                    resta_fecha = fecha_reservacion - fecha_actual

                    if resta_fecha.days < 2 or resta_fecha.days == 0:
                        print("\nLa reservación debe hacerse dos días antes del día elegido.")
                        continue
                    elif resta_fecha.days < 0:
                        print("\nEsa fecha ya paso.")
                        continue
                    
                    break

                while True:

                    turno_reservacion_capturada = input("\nElija un turno por su clave: ")

                    if turno_reservacion_capturada.strip() == "":
                        print("\nNo puede omitirse.")
                        continue
                    
                    try:
                        turno_reservacion = int(turno_reservacion_capturada)
                    except Exception:
                        print("\nNo es de un dato entero.")
                        continue

                    if turno_reservacion in turno_dict:
                        print(f"Turno {turno_dict[turno_reservacion]} seleccionado.")
                        break
                while True:

                    for datos in reservas_dict.values():
                        if fecha_reservacion.strftime("%d/%m/%Y") == datos[0] and clave_de_sala_reservas == datos[1] and turno_dict[turno_reservacion] == datos[4]:
                            print(f"\nEstá ocupada esa sala y turno en la fecha {fecha_reservacion_capturada}.")
                            break
                    else:

                        while True:

                            nombre_evento = input("\nEscribe el nombre del evento: ")

                            if nombre_evento.strip() == "":
                                print("\nNo puede omitirse.")
                                continue

                            break

                        folio = max(reservas_dict.keys(), default=0) + 1

                        reservas_dict[folio] = [fecha_reservacion.strftime("%d/%m/%Y"), clave_de_sala_reservas, clientes_dict[clave_de_cliente_reserva], nombre_evento, turno_dict[turno_reservacion]]
                    break

            elif opcion_menu_reservas.upper() == "B":
                while True:

                    folio_editar_nombre = input("\nDime el folio de la reservacion que quiere editar el nombre: ")

                    if folio_editar_nombre.strip() == "":
                        print("\nNo puede omitirse.")
                        continue

                    try:
                        folio_editar_nombre_int = int(folio_editar_nombre)
                    except Exception:
                        print("\nEl dato no es de tipo entero.")
                        continue

                    for folio, datos in reservas_dict.items():
                        if folio_editar_nombre_int == folio:
                            nombre_actualizado = input("\nEscribe el nuevo nombre del evento: ")
                            datos[3] = nombre_actualizado
                            break
                        else:
                            print("\nNo existe el folio proporcionado.")
                            break
                    
                    print("\nNombre editado.")
                    break

            elif opcion_menu_reservas.upper() == "C":
                pass
            elif opcion_menu_reservas.upper() == "D":
                break
            else:
                print("\nElija una opcion correcta.")

    elif opcion_menu.upper() == "B":
        while True:

            print("""
    --------------------------------MENU REPORTES--------------------------------\n
    [A] REPORTE EN PANTALLA DE RESERVACIONES PARA UNA FECHA\n
    [B]	EXPORTAR REPORTE TABULAR EN EXCEL\n
    [C]	VOLVER AL MENU PRINCIPAL\n
    """)

            opcion_menu_reportes = input("\nElija una opcion: ")

            if opcion_menu_reportes.upper() == "A":
                while True:

                    fecha_a_consultar_capturada = input("\nFecha que desea consultar si hay reservaciones: ")

                    if fecha_a_consultar_capturada.strip() == "":
                        print("\nNo se puede omitir.")
                        continue
                    
                    try:
                        fecha_a_consultar = datetime.datetime.strptime(fecha_a_consultar_capturada, "%d/%m/%Y").date()
                    except Exception:
                        print("\nFormato de fecha no correcto.")
                        continue

                    consulta_reservaciones = list()

                    for datos in reservas_dict.values():
                        if fecha_reservacion_capturada == datos[0]:
                            consulta_reservaciones.append([datos[1],datos[2],datos[3],datos[4]])
                            continue
                    if len(consulta_reservaciones) == 0:
                        print("No hay reservaciones en esa fecha")
                        break

                    print("*" * 100)
                    print(f"{'REPORTE DE RESERVACIONES PARA EL DIA ' + fecha_a_consultar_capturada:^100}")
                    print("*" * 100)
                    print(f"{'SALA':<15}{'CLIENTE':<20}{'EVENTO':<50}TURNO")
                    print("*" * 100)
                    for datos in consulta_reservaciones:
                        print(f"{datos[0]:<15}{datos[1]:<20}{datos[2]:<50}{datos[3]}")
                    print("*" * 100)
                    break

            elif opcion_menu_reportes.upper() == "B":
                pass
            elif opcion_menu_reportes.upper() == "C":
                break
            else:
                print("\nElija una opcion correcta.")

    elif opcion_menu.upper() == "C":
        while True:
            nombre_cliente = input("\nEscribe el nombre del cliente: ")

            if nombre_cliente.strip() == "":
                print("\nNo se puede omitir.")
                continue

            clave_de_cliente = max(clientes_dict.keys(), default=0) + 1

            clientes_dict[clave_de_cliente] = nombre_cliente

            print(f"\nSu clave es: {clave_de_cliente}")

            print(clientes_dict)

            break
    elif opcion_menu.upper() == "D":
        while True:

            sala_nombre = input("\nNombre de sala: ")

            if sala_nombre.strip() == "":
                print("\nNo puede omitirse.")
                continue
            break

        while True:

            cupo_de_sala_capturada = input("\nCupo de la sala: ")

            if cupo_de_sala_capturada.strip() == "":
                print("\nNo puede omitirse.")
                continue

            try:
                cupo_de_sala = int(cupo_de_sala_capturada)
            except Exception:
                print("\nNo es de tipo entero.")
            
            if cupo_de_sala <= 0:
                print("\nNo puede ser menor a cero.")
                continue

            clave_de_sala = max(salas_dict.keys(), default=0) + 1

            salas_dict[clave_de_sala] = (sala_nombre, cupo_de_sala)

            print(f"\nEl numero de sala es: {clave_de_sala}")

            print(salas_dict)

            break
            
    elif opcion_menu.upper() == "E":

        with open("clientes.csv","w", newline="") as archivo:
            grabador = csv.writer(archivo)
            grabador.writerow(("clave", "nombre"))
            grabador.writerows([(clave, dato) for clave, dato in clientes_dict.items()])

        with open("salas.csv","w", newline="") as archivo:
            grabador = csv.writer(archivo)
            grabador.writerow(("clave", "nombre", "cupo"))
            grabador.writerows([(clave, datos[0], datos[1]) for clave, datos in salas_dict.items()])

        with open("reservas.csv","w", newline="") as archivo:
            grabador = csv.writer(archivo)
            grabador.writerow(("clave", "fecha", "sala", "cliente", "evento", "turno"))
            grabador.writerows([(folio, datos[0], datos[1], datos[2], datos[3], datos[4]) for folio, datos in reservas_dict.items()])

        print("\nFin del programa.")
        break
    else:
        print("\nElija una opcion correcta.")