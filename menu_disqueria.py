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
    print("(1) Sí\n(2) No")
    inicio = input("Elije una opción para entrar al sistema: ")
    while inicio == '1':
        opcion = menu()
        if opcion not in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
            print(" ")
            print("--")
            print("Intente nuevamente.")
            print("Ingrese una opcion valida.")
            print("--")
            print(" ")
            pass
        while opcion in ['1','2','3','4','5','6','7','8','9','10','11','12','13']:
            if opcion == "1":
                # Dar de alta un álbum
                id_album = input("ID del álbum: ")
                nombre_album = input("Nombre del álbum: ")
                artista = input("Nombre del Artista: ")
                genero_musical = input("Género musical: ")
                categoria = input("Categoría: ")
                stock = input("Cantidad de producto: ")
                precio_de_compra = float(input("Precio de compra: "))
                precio_venta_cliente = float(input("Precio de venta: "))
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
                    nuevo_stock = input("Nueva cantidad de producto: ")
                    nuevo_precio_compra = float(input("Nuevo precio de compra: "))
                    nuevo_precio_venta = float(input("Nuevo precio de venta: "))
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
                disqueria.mostrar_albumes()

            elif opcion == "6":
                # Dar de alta empleado
                nombre = input("Nombre del empleado: ")
                dni = input("DNI del empleado: ")
                telefono = input("Teléfono del empleado: ")
                direccion = input("Dirección del empleado: ")
                cargo = input("Cargo asignado: ")
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
                # Modificar empleado
                dni_empleado = input("Inserte el dni del empleado a modificar: ")
                if disqueria.contiene_empleado(dni_empleado):
                    nuevo_nombre = input("Nuevo nombre del empleado: ")
                    nuevo_telefono = input("Nuevo telefono del empleado: ")
                    nueva_direccion = input("Nueva direccion del empleado: ")
                    nuevo_cargo = input("Nuevo cargo del empleado: ")
                    nuevo_dinero_aportado = input("Nuevo dinero aportado: ")
                    empleado = disqueria.buscar_empleado(dni_empleado)
                    empleado.nombre = nuevo_nombre
                    empleado.telefono = nuevo_telefono
                    empleado.direccion = nueva_direccion
                    empleado.cargo = nuevo_cargo
                    empleado.dinero_aportado = nuevo_dinero_aportado
                    print("Empleado modificado con éxito.")
                else:
                    print("El empleado no existe en la disquería.")
                    
                 

            elif opcion == "9":
                # Buscar empleado
                dni_empleado = input("Insertar el DNI del empleado: ")
                if disqueria.contiene_empleado(dni_empleado):
                    disqueria.buscar_empleado(dni_empleado)
                else:
                    print("No se encuentra el empleado")

            elif opcion == "10":
                # Listar empleados
                disqueria.mostrar_empleados()

            elif opcion == "11":
                # Guardar archivo
                disqueria.guardar_archivo()

            elif opcion == "12":
                # Leer archivo
                disqueria.leer_archivo()

            opcion = menu()

if __name__ == "__main__":
    disqueria = Disqueria()
    run(disqueria)
