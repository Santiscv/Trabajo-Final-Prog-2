from disqueria import Disqueria, Album, Empleados

def menu():
    print("------ Menú Disqueria ------")
    print("(1)  Dar de alta nuevo Album")
    print("(2)  Dar de baja Album")
    print("(3)  Buscar Album")
    print("(4)  Modificar Album")
    print("(5)  Listar Albums")
    print("(6)  Dar de alta nuevo Empleado")
    print("(7)  Dar de baja Empleado")
    print("(8)  Modificar Empleado")
    print("(9)  Buscar Empleado")
    print("(10) Listar Empleados")
    print("(11) Guardar archivo")
    print("(12) Leer archivo")
    print("(13) Salir")
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
                if opcion not in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
                    print("--")
                    print("Intente nuevamente.")
                    print("Ingrese una opcion valida.")
                    print("--")
                    continue

                if opcion == "1":
                    # Dar de alta un álbum
                    id_album = input("ID del álbum: ")
                    nombre_album = input("Nombre del álbum: ")
                    artista = input("Nombre del Artista: ")
                    genero_musical = input("Género musical: ")
                    categoria = input("Categoría: ")
                    stock = int(input("Cantidad de producto: "))
                    precio_de_compra = float(input("Precio de compra: "))
                    precio_venta_cliente = float(input("Precio de venta: "))
                    
                    try:
                        stock = int(input("Cantidad de producto: "))
                        precio_de_compra = float(input("Precio de compra: "))
                        precio_venta_cliente = float(input("Precio de venta: "))
                    except ValueError:
                        print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                        continue 
                    
                    album = Album(id_album, nombre_album, artista, genero_musical, categoria, stock, precio_de_compra, precio_venta_cliente)
                    
                    if disqueria.contiene_album(album.nombre):
                        print("El Álbum ya existe.")
                    else:
                        disqueria.alta_nuevo_album(album)
                        print("Álbum Agregado")

                elif opcion == "2":
                    # Dar de baja un álbum
                    id_album = input("Inserte el ID del álbum: ")
                    if disqueria.contiene_album(id_album):
                        disqueria.eliminar_album(id_album)
                        print("Álbum dado de baja")
                    else:
                        print("El álbum no existe")

                elif opcion == "3":
                    # Buscar álbum
                    id_album = input("Inserte el ID del álbum: ")
                    if disqueria.contiene_album(id_album):
                        disqueria.buscar_album(id_album)
                    else:
                        print("No se encuentra el álbum")

                elif opcion == "4":
                    # Modificar álbum
                    id_album = input("Inserte el ID del álbum a modificar: ")
                    if disqueria.contiene_album(id_album):
                        nuevo_nombre = input("Nuevo nombre del álbum: ")
                        nuevo_artista = input("Nuevo nombre del artista: ")
                        nuevo_genero_musical = input("Nuevo género musical: ")
                        nueva_categoria = input("Nueva categoría: ")
                        nuevo_stock = int(input("Nueva cantidad de producto: "))
                        nuevo_precio_compra = float(input("Nuevo precio de compra: "))
                        nuevo_precio_venta = float(input("Nuevo precio de venta: "))
                        try:
                            nuevo_stock = int(input("Nueva cantidad de producto: "))
                            nuevo_precio_compra = float(input("Nuevo precio de compra: "))
                            nuevo_precio_venta = float(input("Nuevo precio de venta: "))
                            
                        except ValueError:
                            print("Error: Ingrese el valor correctamente, intentelo de nuevo")
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
                        print("Álbum modificado con éxito.")
                    else:
                        print("El álbum no existe en la disquería.")

                elif opcion == "5":
                    # Listar álbumes
                    if len(disqueria.arbol_album) == 0:
                        print("No hay álbumes disponibles.")
                    else:
                        disqueria.mostrar_albumes()

                elif opcion == "6":
                    # Dar de alta empleado
                    nombre = input("Nombre del empleado: ")
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    dni = int(input("DNI del empleado: "))
                    print("NOTA: El telefono no tiene que tener simbolo + o separacion de puntos")
                    telefono = int(input("Teléfono del empleado: "))
                    direccion = input("Dirección del empleado: ")
                    cargo = input("Cargo asignado: ")
                    try:
                        dni = int(input("DNI del empleado: "))
                        telefono = int(input("Teléfono del empleado: "))
                    except ValueError:
                        print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                        continue 
                    empleado = Empleados(nombre, dni, telefono, direccion, cargo)
                    
                    if disqueria.contiene_empleado(empleado.dni):
                        print("El empleado ya existe.")
                    else:
                        disqueria.alta_nuevo_empleado(empleado)
                        print("Empleado dado de alta.")

                elif opcion == "7":
                    # Dar de baja empleado
                    dni_empleado = input("Inserte el DNI del empleado: ")
                    if disqueria.contiene_empleado(dni_empleado):
                        disqueria.eliminar_empleado(dni_empleado)
                        print("Empleado dado de baja.")
                    else:
                        print("El empleado no existe.")

                elif opcion == "8":
                    pass
                    # Modificar empleado (pendiente)

                elif opcion == "9":
                    # Buscar empleado
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    dni_empleado = int(input("Insertar el DNI del empleado: "))
                    try:
                       dni_empleado = int(input("Insertar el DNI del empleado: "))
                    except ValueError:
                        print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                        continue 
                    if disqueria.contiene_empleado(dni_empleado):
                        disqueria.buscar_empleado(dni_empleado)
                    else:
                        print("No se encuentra el empleado")

                elif opcion == "10":
                    if len(disqueria.arbol_empleado) == 0:
                        print("No hay empleados cargados en el sistema")
                    else:    
                        disqueria.mostrar_empleados()

                elif opcion == "11":
                    # Guardar archivo
                    disqueria.guardar_archivo()

                elif opcion == "12":
                    # Leer archivo
                    disqueria.leer_archivo()

                elif opcion == "13":
                    print("--")
                    print("Saliendo del programa.")
                    print("--")
                    break


if __name__ == "__main__":
    disqueria = Disqueria()
    run(disqueria)
