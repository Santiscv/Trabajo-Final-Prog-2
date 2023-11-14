from disqueria import Disqueria, Album, Empleados

def menu():
    print("------ Menú Disqueria ------")
    print("(1)  Dar de alta nuevo Album")
    print("(2)  Dar de baja Album")
    print("(3)  Buscar Album")
    print("(4)  Modificar Album")
    print("(5)  Listar Albums")
    print("----------Empleado--------")
    print("(6)  Dar de alta nuevo Empleado")
    print("(7)  Dar de baja Empleado")
    print("(8)  Modificar Empleado")
    print("(9)  Buscar Empleado")
    print("(10) Listar Empleados")
    print("---------Avanzados--------")
    print("(11) Venta de album")
    print("(12) Presupuesto disqueria")
    print("---------Extras--------")
    print("(13) Guardar archivo")
    print("(14) Leer archivo")
    print("(15) Salir")
    print("---------------------------")
    opcion = input("Elija una opcion: ")
    print("---------------------------")
    return opcion

def run(disqueria):
    print("Hellfish Disquerias")
    while True:
        inicio = input("(1) Sí\n(2) No\nElija una opción para entrar al sistema: ")
        if inicio == '2':
            print("--")
            print("Programa finalizado")
            print("--")
            break
        elif inicio == '1':
            while True:
                opcion = menu()
                if opcion not in ['1','2','3','4','5','6','7','8','9','10','11','12','13', '14','15']:
                    print("--")
                    print("Intente nuevamente.")
                    print("Ingrese una opcion valida.")
                    print("--")
                    continue

                if opcion == "1":
                    # Dar de alta un álbum
                    id_album = int(input("ID del álbum: "))
                    nombre_album = input("Nombre del álbum: ")
                    artista = input("Nombre del Artista: ")
                    genero_musical = input("Género musical: ")
                    categoria = input("Categoría: ")

                    try:
                        stock = int(input("Cantidad de producto: "))
                        precio_de_compra = float(input("Precio de compra: "))
                        precio_venta_cliente = float(input("Precio de venta: "))
                    except ValueError:
                        print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                        continue 
                    
                    album = Album(id_album, nombre_album, artista, genero_musical, categoria, stock, precio_de_compra, precio_venta_cliente)
                    
                    if disqueria.contiene_album(album.nombre):
                        print("--")
                        print("El Álbum ya existe.")
                        print("--")
                    else:
                        disqueria.alta_nuevo_album(album)
                        print("--")
                        print("Álbum Agregado")
                        print("--")

                elif opcion == "2":
                    # Dar de baja un álbum
                    id_album = input("Inserte el ID del álbum: ")
                    if disqueria.contiene_album(id_album):
                        disqueria.eliminar_album(id_album)
                        print("--")
                        print("Álbum dado de baja")
                        print("--")
                    else:
                        print("--")
                        print("El álbum no existe")
                        print("--")

                elif opcion == "3":
                    # Buscar álbum
                    id_album = int(input("Inserte el ID del álbum: "))
                    if disqueria.contiene_album(id_album):
                        disqueria.buscar_album(id_album)
                    else:
                        print("--")
                        print("No se encuentra el álbum")
                        print("--")
                        
                elif opcion == "4":
                    # Modificar álbum
                    id_album = int(input("Inserte el ID del álbum a modificar: "))
                    if disqueria.contiene_album(id_album):
                        nuevo_nombre = input("Nuevo nombre del álbum: ")
                        nuevo_artista = input("Nuevo nombre del artista: ")
                        nuevo_genero_musical = input("Nuevo género musical: ")
                        nueva_categoria = input("Nueva categoría: ")
                        try:
                            nuevo_stock = int(input("Nueva cantidad de producto: "))
                            nuevo_precio_compra = float(input("Nuevo precio de compra: "))
                            nuevo_precio_venta = float(input("Nuevo precio de venta: "))
                            
                        except ValueError:
                            print("--")
                            print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                            print("--")
                            continue 
                        
                        print("--")
                        print("Valores anteriores")
                        print("--")
                        
                        album = disqueria.buscar_album(id_album)
                
                        album.nombre = nuevo_nombre
                        album.artista = nuevo_artista
                        album.genero_musical = nuevo_genero_musical
                        album.categoria = nueva_categoria
                        album.stock = nuevo_stock
                        album.precio_compra_tienda = nuevo_precio_compra
                        album.precio_venta_cliente = nuevo_precio_venta
                        
                        print("--")
                        print("Álbum modificado con éxito.")
                        print("--")
                    else:
                        print("--")
                        print("El álbum no existe en la disquería.")
                        print("--")
                        

                elif opcion == "5":
                    # Listar álbumes
                    if len(disqueria.arbol_album) == 0:
                        print("--")
                        print("No hay álbumes disponibles.")
                        print("--")
                        
                    else:
                        disqueria.mostrar_albumes()

                elif opcion == "6":
                    # Dar de alta empleado
                    nombre = input("Nombre del empleado: ")
                    try:
                        print("NOTA: El DNI no tiene que estar separado de puntos ")
                        dni = int(input("DNI del empleado: "))
                        print("NOTA: El telefono no tiene que tener simbolo + o separacion de puntos")
                        telefono = int(input("Teléfono del empleado: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                        print("--")
                        continue 
                        
                    direccion = input("Dirección del empleado: ")
                    cargo = input("Cargo asignado: ")
                    empleado = Empleados(nombre, dni, telefono, direccion, cargo)
                    
                    if disqueria.contiene_empleado(empleado.dni):
                        print("--")
                        print("El empleado ya existe.")
                        print("--")
                        
                    else:
                        disqueria.alta_nuevo_empleado(empleado)
                        print("--")
                        print("Empleado dado de alta.")
                        print("--")
                        

                elif opcion == "7":
                    # Dar de baja empleado
                    dni_empleado = int(input("Inserte el DNI del empleado: "))
                    if disqueria.contiene_empleado(dni_empleado):
                        disqueria.eliminar_empleado(dni_empleado)
                        print("--")
                        print("Empleado dado de baja.")
                        print("--")
                        
                    else:
                        print("--")
                        print("El empleado no existe.")
                        print("--")

                elif opcion == "8":
                    dni_e = int(input("Inserte el DNI del empleado a modificar: "))
                    if disqueria.contiene_empleado(dni_e):
                        nuevo_nombre = input("Nuevo nombre del empleado: ")
                        nuevo_telefono = int(input("Nuevo telefono del empleado: "))
                        nueva_direccion = (input("Nueva direccion del empleado: "))
                        nuevo_cargo = input("Nuevo cargo del empleado: ")
                        try:
                            nuevo_telefono = int(input("Nuevo telefono del empleado: "))
                            
                        except ValueError:
                            print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                            continue 
                        
                        print("--")
                        print(f"Se modificaron los valores anteriores del empleado con dni {dni_e}.")
                        print("--")

                        empleado = disqueria.buscar_empleado2(dni_e) # buscar_empleado2() no imprime los valores. el que si lo hace es buscar_empleado()
                
                        empleado.nombre = nuevo_nombre
                        empleado.telefono = nuevo_telefono
                        empleado.direccion = nueva_direccion
                        empleado.cargo = nuevo_cargo
                        
                        print("Empleado modificado con éxito.")
                    else:
                        print("El empleado no está cargado en la disquería.")
                    # Modificar empleado (pendiente)

                elif opcion == "9":
                    # Buscar empleado
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    try:
                       dni_empleado = int(input("Insertar el DNI del empleado: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                        print("--")
                        continue 
                        
                    if disqueria.contiene_empleado(dni_empleado):
                        disqueria.buscar_empleado(dni_empleado)
                    else:
                        print("--")
                        print("No se encuentra el empleado")
                        print("--")
                        

                elif opcion == "10":
                    if len(disqueria.arbol_empleado) == 0:
                        print("--")
                        print("No hay empleados cargados en el sistema")
                        print("--")
                    else:    
                        disqueria.mostrar_empleados()

                elif opcion == "11":
                    # Venta de Album
                    try:
                        print("NOTA: El ID del album no contiene ninguna letra o caracter especial")
                        id_album = int(input("ID del álbum a vender: "))
                        cantidad = int(input("Cantidad de unidades a vender: "))
                        print("NOTA: El DNI no tiene que estar separado de puntos ")
                        dni_empleado = int(input("DNI del empleado que realiza la venta: "))
                    except ValueError:
                        print("Ingrese los valores correctos")
                        
                    album = disqueria.buscar_album2(id_album)
                    if not album:
                        print("--")
                        print("Error: No se encontró el álbum.")
                        print("--")
                    else:
                        empleado = disqueria.buscar_empleado2(dni_empleado)
                        if not empleado:
                            print("--")
                            print("Error: No se encontró al empleado.")
                            print("--")
                        else:
                            # Verificar si hay suficiente stock
                            if cantidad <= 0:
                                print("Error: La cantidad debe ser mayor que cero.")
                            elif album.stock < cantidad:
                                print("--")
                                print("Error: Unidades insuficientes para realizar la venta.")
                                print("NOTA: Debe reponer el stock.")
                                print("--")
                            else:
                                # Realizar la venta
                                print(f"\nRealizando venta de {cantidad} unidades del álbum {album.nombre}.")
            
                                disqueria.venta_album(id_album, cantidad, dni_empleado)
                                
                                print("--")
                                print(f"\nVenta exitosa. Total recaudado: {album.precio_venta_cliente * cantidad}")
                                print("--")
                
                elif opcion == "12":
                    disqueria.imprimir_presupuesto()
                    
                elif opcion == "13":
                    # Guardar archivo
                    print("--")
                    print("Los datos han sidos guardados con exito!.")
                    print("--")
                    disqueria.guardar_archivo()

                elif opcion == "14":
                    # Leer archivo
                    print("--")
                    print("Datos leidos con exito!")
                    print("--")
                    disqueria.leer_archivo()

                
                elif opcion == "15":
                    print("--")
                    print("Saliendo del programa.")
                    print("--")
                    break


if __name__ == "__main__":
    disqueria = Disqueria()
    run(disqueria)