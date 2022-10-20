import csv
import datetime
import os
import openpyxl

clientes_dict = dict()
salas_dict = dict()
reservas_dict = dict()
turno_dict = {1: "Matutino", 2: "Vespertino", 3: "Nocturno"}

consulta_reservaciones = list()

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
            reservas_dict[int(folio)] = [fecha, int(sala), cliente, evento, turno]
else:
    print("\nEs la primera vez que se ejecuta el programa.")
while True:

    print("""
    --------------------------------MENÚ PRINCIPAL--------------------------------\n
    [A] RESERVACIONES.\n
    [B]	REPORTES.\n
    [C]	REGISTRAR NUEVO CLIENTE.\n
    [D]	REGISTRAR NUEVA SALA.\n
    [E] Salir
    """)

    opcion_menu = input("\nSeleccione una opción: ")

    if opcion_menu.upper() == "A":
        while True:

            print("""
    --------------------------------MENÚ RESERVAS--------------------------------\n
    [A] REGISTRAR NUEVA RESERVACIÓN\n
    [B]	MODIFICAR DESCRIPCION DE UNA RESERVACIÓN\n
    [C]	CONSULTAR DISPONIBIBLIDAD DE SALAS PARA UNA FECHA\n
    [D]	VOLVER AL MENÚ PRINCIPAL
    """)

            opcion_menu_reservas = input("Elija una opción: ")

            if opcion_menu_reservas.upper() == "A":
                print(f"\n{'Clientes registrados':^40}")
                print("-" * 40)
                print("Clave\t\tCliente")
                print("-" * 40)
                for clave, nombre in clientes_dict.items():
                    print(f"{clave}\t\t{nombre}")
                print("-" * 40)
                while True:

                    clave_de_cliente_reserva_capturada = input("\nIngresa la clave del cliente: ")

                    if clave_de_cliente_reserva_capturada.strip() == "":
                        print("\nLa clave no puede omitirse.")
                        continue

                    try:
                        clave_de_cliente_reserva = int(clave_de_cliente_reserva_capturada)
                    except Exception:
                        print("\nLa clave no es de tipo entero.")
                        continue

                    if clave_de_cliente_reserva in clientes_dict:
                        print(f"\nCliente {clientes_dict[clave_de_cliente_reserva]} puede hacer la reservación.")
                        break
                    else:
                        print("\nClave cliente no existe.")
                        continue

                while True:
                    
                    print(f"\n{'Salas registrados':^40}")
                    print("-" * 40)
                    print(f"{'Clave':<10}{'Nombre':<25}{'Cupo'}")
                    print("-" * 40)
                    for clave, nombre_cupo in salas_dict.items():
                        print(f"{clave:<10}{nombre_cupo[0]:<25}{nombre_cupo[1]}")
                    print("-" * 40)

                    clave_de_sala_reservas_capturada = input("\nIngresa el número de sala: ")

                    if clave_de_sala_reservas_capturada.strip() == "":
                        print("\nEl número de sala no puede omitirse.")
                        continue

                    try:
                        clave_de_sala_reservas = int(clave_de_sala_reservas_capturada)
                    except Exception:
                        print("\nEl número no es de tipo entero.")
                        continue

                    if clave_de_sala_reservas in salas_dict:
                        print(f"\nSala {clave_de_sala_reservas} seleccionada.")
                        break
                    else:
                        print("\nClave de sala no existe.")
                        continue

                while True:

                    fecha_actual = datetime.date.today()

                    fecha_reservacion_capturada = input("\nEscribe la fecha de reservación que desea con el formato dd/mm/aaaa: ")

                    if fecha_reservacion_capturada.strip() == "":
                        print("\nLa fecha no puede omitirse.")
                        continue

                    try:
                        fecha_reservacion = datetime.datetime.strptime(fecha_reservacion_capturada, "%d/%m/%Y").date()
                    except Exception:
                        print("\nFormato de fecha incorrecto.")
                        continue

                    resta_fecha = fecha_reservacion - fecha_actual

                    if resta_fecha.days < 2 and resta_fecha.days > 0:
                        print("\nLa reservación debe hacerse dos días antes del día elegido.")
                        continue
                    elif resta_fecha.days < 0:
                        print("\nEsa fecha ya pasó.")
                        continue
                    
                    break

                while True:

                    print(f"\n{'Clientes registrados':^40}")
                    print("-" * 40)
                    print("Clave\t\tTurno")
                    print("-" * 40)
                    for clave, turno in turno_dict.items():
                        print(f"{clave}\t\t{turno}")
                    print("-" * 40)

                    turno_reservacion_capturada = input("\nElija un turno por su clave: ")

                    if turno_reservacion_capturada.strip() == "":
                        print("\nEl turno no puede omitirse.")
                        continue
                    
                    try:
                        turno_reservacion = int(turno_reservacion_capturada)
                    except Exception:
                        print("\nNo es de un dato entero.")
                        continue

                    if turno_reservacion in turno_dict:
                        print(f"\nTurno {turno_dict[turno_reservacion]} seleccionado.")
                        break
                    else:
                        print("\nEl turno no existe.")
                        continue
                while True:

                    for datos in reservas_dict.values():
                        if fecha_reservacion.strftime("%d/%m/%Y") == datos[0] and clave_de_sala_reservas == datos[1] and turno_dict[turno_reservacion] == datos[4]:
                            print(f"\nEstá ocupada esa sala y turno en la fecha {fecha_reservacion_capturada}.")
                            break
                    else:

                        while True:

                            nombre_evento = input("\nIngrese el nombre del evento: ")

                            if nombre_evento.strip() == "":
                                print("\nEl nombre no puede omitirse.")
                                continue

                            break

                        folio = max(reservas_dict.keys(), default=0) + 1

                        reservas_dict[folio] = [fecha_reservacion.strftime("%d/%m/%Y"), clave_de_sala_reservas, clientes_dict[clave_de_cliente_reserva], nombre_evento, turno_dict[turno_reservacion]]
                    break

            elif opcion_menu_reservas.upper() == "B":
                while True:
                    print(f"\n{'Modificar nombre':^50}")
                    print("-" * 50)
                    print(f"{'Folio':<10}{'Nombre evento'}")
                    print("-" * 50)
                    for folio, nombre_evento in reservas_dict.items():
                        print(f"{folio:<10}{nombre_evento[3]}")
                    print("-" * 50)
                    folio_editar_nombre = input("\nIngresa el folio de la reservación que quiere editar el nombre: ")

                    if folio_editar_nombre.strip() == "":
                        print("\nEl folio no puede omitirse.")
                        continue

                    try:
                        folio_editar_nombre_int = int(folio_editar_nombre)
                    except Exception:
                        print("\nEl dato no es de tipo entero.")
                        continue
                    
                    if folio_editar_nombre_int in reservas_dict:
                        for folio, datos in reservas_dict.items():
                            if folio == folio_editar_nombre_int:
                                nombre_actualizado = input("\nIngrese el nuevo nombre del evento: ")
                                datos[3] = nombre_actualizado
                                print("\nNombre editado.")
                                break
                    else:
                        print("\nNo existe el folio.")
                        continue
                            
                    break

            elif opcion_menu_reservas.upper() == "C":
                while True:
                    listas_ocupadas = list()
                    lista_posibles = list()

                    fecha_para_ver_disponibles_capturada = input("\nIngrese la fecha donde quiera ver la disponibilidad: ")

                    if fecha_para_ver_disponibles_capturada.strip() == "":
                        print("\nLa fecha no puede omitise.")
                        continue

                    try:
                        fecha_para_ver_disponibles = datetime.datetime.strptime(fecha_para_ver_disponibles_capturada, "%d/%m/%Y").date()
                    except Exception:
                        print("\nFormato de fecha incorrecto.")
                        continue

                    for clave, valor in reservas_dict.items():
                        fecha, sala, turno = (valor[0], valor[1], valor[4])
                        if fecha == fecha_para_ver_disponibles_capturada:
                            listas_ocupadas.append((sala, turno))
                    
                    reservas_ocupadas = set(listas_ocupadas)

                    for sala in salas_dict:
                        for turno in turno_dict:
                            lista_posibles.append((sala, turno_dict[turno]))
                    
                    reservas_posibles = set(lista_posibles)

                    reservaciones_disponibles = sorted(list(reservas_posibles - reservas_ocupadas))

                    print(f"\n** Salas disponibles para renta el {fecha_para_ver_disponibles_capturada} **")
                    print(f"\n{'SALA':<20}{'TURNO':>20}")
                    for sala, turno in reservaciones_disponibles:
                        print(f"{sala},{salas_dict[sala][0]:<20}{turno:>20}")
                    break
            elif opcion_menu_reservas.upper() == "D":
                break
            else:
                print("\nElija una opción correcta.")

    elif opcion_menu.upper() == "B":
        while True:

            print("""
    --------------------------------MENÚ REPORTES--------------------------------\n
    [A] REPORTE EN PANTALLA DE RESERVACIONES PARA UNA FECHA\n
    [B]	EXPORTAR REPORTE TABULAR EN EXCEL\n
    [C]	VOLVER AL MENÚ PRINCIPAL\n
    """)

            opcion_menu_reportes = input("\nElija una opción: ")

            if opcion_menu_reportes.upper() == "A":
                while True:

                    consulta_reservaciones.clear()

                    fecha_a_consultar_capturada = input("\nFecha que desea consultar si hay reservaciones: ")

                    if fecha_a_consultar_capturada.strip() == "":
                        print("\nNo se puede omitir la fecha.")
                        continue
                    
                    try:
                        fecha_a_consultar = datetime.datetime.strptime(fecha_a_consultar_capturada, "%d/%m/%Y").date()
                    except Exception:
                        print("\nFormato de fecha incorrecto.")
                        continue

                    
                    for datos in reservas_dict.values():
                        if fecha_a_consultar_capturada == datos[0]:
                            consulta_reservaciones.append([datos[1],datos[2],datos[3],datos[4]])
                            continue
                    if len(consulta_reservaciones) == 0:
                        print("No hay reservaciones en esa fecha.")
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
                libro = openpyxl.Workbook()
                hoja = libro["Sheet"] 
                hoja.title = "Primera"
                hoja.append(("sala", "cliente", "evento", "turno"))
                for valores in consulta_reservaciones:
                    hoja.append(valores)
                libro.save("reservas_tabular.xlsx")
                print("\nExportado a Excel correctamente.")
            elif opcion_menu_reportes.upper() == "C":
                break
            else:
                print("\nElija una opción correcta.")

    elif opcion_menu.upper() == "C":
        while True:
            nombre_cliente = input("\nIngresa el nombre del cliente: ")

            if nombre_cliente.strip() == "":
                print("\nEl nombre no se puede omitir.")
                continue

            clave_de_cliente = max(clientes_dict.keys(), default=0) + 1

            clientes_dict[clave_de_cliente] = nombre_cliente

            print(f"\nSu clave es: {clave_de_cliente}")

            break
    elif opcion_menu.upper() == "D":

        while True:

            sala_nombre = input("\nNombre de sala: ")

            if sala_nombre.strip() == "":
                print("\nNo puede omitirse el nombre de la sala.")
                continue

            break

        while True:

            cupo_de_sala_capturada = input("\nCupo de la sala: ")

            if cupo_de_sala_capturada.strip() == "":
                print("\nNo puede omitirse el cupo de la sala.")
                continue

            try:
                cupo_de_sala = int(cupo_de_sala_capturada)
            except Exception:
                print("\nNo es de tipo entero.")
            
            if cupo_de_sala <= 0:
                print("\nEl cupo de la sala debe ser mayor a cero.")
                continue

            clave_de_sala = max(salas_dict.keys(), default=0) + 1

            salas_dict[clave_de_sala] = (sala_nombre, cupo_de_sala)

            print(f"\nEl número de sala es: {clave_de_sala}")

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

        print("\nDatos preservados en CSV.")
        print("\nFIN DEL PROGRAMA\n")
        break
    else:
        print("\nElija una opción correcta.")