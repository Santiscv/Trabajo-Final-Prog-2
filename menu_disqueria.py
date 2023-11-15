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
        while inicio == '1':
                opcion = menu()
                if opcion not in ['1','2','3','4','5','6','7','8','9','10','11','12','13', '14','15']:
                    print("--")
                    print("Intente nuevamente.")
                    print("Ingrese una opcion valida.")
                    print("--")
                    continue

                if opcion == "1":
                    # Dar de alta un álbum
                    nombre_album = input("Nombre del álbum: ")
                    artista = input("Nombre del Artista: ")
                    genero_musical = input("Género musical: ")
                    print("--")
                    print("Categorias") 
                    print("(1) CD\n(2) Vinilo\n")
                    categoria = None
                    while categoria is None:
                        try:
                            categoria = int(input("Elija una opción en las categorias: "))
                        except ValueError:
                            print("--")
                            print("(1) CD\n(2) Vinilo\n")
                            print("--")
                            print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                            print("--")
                            categoria=None

                    id_album = None
                    while id_album is None:
                        print("--")
                        print("NOTA: El ID del album no contiene ninguna letra o caracter especial")
                        print("--")
                        try:
                            id_album = int(input("ID del álbum: "))
                        except ValueError:
                            print("--")
                            print("Error: El ID del album no contiene ninguna letra o caracter especial")
                            print("--")
                            id_album = None 
                    stock = None
                    while stock is None:
                        try:
                            stock = int(input("Cantidad de unidades: "))
                        except ValueError:
                            print("--")
                            print("Ingrese el valor correctamente, intentelo de nuevo")
                            print("--")
                            stock = None 
                    try:
                        precio_de_compra = float(input("Precio de compra c/u: "))
                        precio_venta_cliente = float(input("Precio de venta: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                        print("--")
                        continue 
                    while precio_venta_cliente <= precio_de_compra or precio_venta_cliente<=0 and precio_de_compra<0:
                        print("--")
                        print("NOTA: No puede introducir valores negativos")
                        print("NOTA: El valor de la venta debe ser mayor que el valor de la compra")
                        print("--")
                        precio_de_compra = float(input("Precio de compra c/u: "))
                        precio_venta_cliente = float(input("Precio de venta: "))
                    
                    if precio_de_compra < precio_venta_cliente:
                        album = Album(id_album, nombre_album, artista, genero_musical, categoria, stock, precio_de_compra, precio_venta_cliente)

                        if disqueria.contiene_album(album.id):
                            print("--")
                            print("El Álbum ya existe.")
                            print("--")
                        else:
                            if disqueria.presupuesto_disqueria - album.precio_compra_tienda >= 0:
                                disqueria.presupuesto_disqueria -= album.precio_compra_tienda * album.stock
                                disqueria.alta_nuevo_album(album)
                                print("--")
                                print("Álbum Agregado")
                                print(f"Presupuesto en caja actualizado: {disqueria.presupuesto_disqueria}")
                                print("--")
                            else:
                                print("--")
                                print("Error: Presupuesto insuficiente para agregar el álbum.")
                                print("--")
                
                elif opcion == "2":
                    # Dar de baja un álbum
                    print("NOTA: El ID del album no contiene ninguna letra o caracter especial")
                    try:
                        id_album = int(input("Inserte el ID del álbum: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el ID correctamente, Corroborelo")
                        print("--")
                        continue 
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
                    print("NOTA: El ID del album no contiene ninguna letra o caracter especial")
                    try:
                        id_album = int(input("Inserte el ID del álbum: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el ID correctamente, Corroborelo")
                        print("--")
                        continue 
                    
                    if disqueria.contiene_album(id_album):
                        disqueria.buscar_album(id_album)
                    else:
                        print("--")
                        print("No se encuentra el álbum")
                        print("--")
                        
                elif opcion == "4":
                    # Modificar álbum
                    print("NOTA: El ID del album no contiene ninguna letra o caracter especial")
                    try:
                        id_album = int(input("Inserte el ID del álbum a modificar: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el ID correctamente, intentelo de nuevo")
                        print("--")
                        continue 
                    
                    print("--")
                    print("Valores anteriores")
                    print("--")
                        
                    album = disqueria.buscar_album(id_album)
                    
                    if disqueria.contiene_album(id_album):
                        modificar_nombre_album = input("¿Desea modificar el nombre del álbum? (S/N): ")
                        if modificar_nombre_album.lower() == 's':
                            nuevo_nombre = input("Nuevo nombre del álbum: ")
                            album.nombre = nuevo_nombre

                        modificar_artista = input("¿Desea modificar el nombre del artista? (S/N): ")
                        if modificar_artista.lower() == 's':
                            nuevo_artista = input("Nuevo nombre del artista: ")
                            album.artista = nuevo_artista
                        
                        modificar_genero = input("¿Desea modificar el genero? (S/N): ")
                        if modificar_genero.lower() == 's':
                            nuevo_genero_musical = input("Nuevo género musical: ")
                            album.genero_musical = nuevo_genero_musical
                            
                        modificar_categoria = input("¿Desea modificar la categoria? (S/N): ")
                        if modificar_categoria.lower() == 's':
                            print("--")
                            print("Categorias") 
                            print("(1) CD\n(2) Vinilo\n")
                            nueva_categoria = None
                            while nueva_categoria is None:
                                try:
                                    nueva_categoria = int(input("Nueva categoría: "))
                                    album.categoria = nueva_categoria
                                except ValueError:
                                    print("--")
                                    print("(1) CD\n(2) Vinilo\n")
                                    print("--")
                                    print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                                    print("--")
                                    nueva_categoria=None
                        
                        modificar_stock = input("¿Desea modificar el stock? (S/N): ")
                        if modificar_stock.lower() == 's':
                            nuevo_stock = None
                            while nuevo_stock is None:
                                try:
                                    nuevo_stock = int(input("Nueva cantidad de unidades: "))
                                    album.stock = nuevo_stock
                                except ValueError:
                                    print("--")
                                    print("Ingrese el valor correctamente, intentelo de nuevo")
                                    print("--")
                                    nuevo_stock = None 
                                    
                        modificar_precios = input("¿Desea modificar los precios? (S/N): ")
                        if modificar_precios.lower() == 's':            
                            try:
                                nuevo_precio_compra = float(input("Nuevo precio de compra c/u: "))
                                precio_venta_cliente = float(input("Precio de venta: "))
                                album.precio_compra_tienda = nuevo_precio_compra
                                album.precio_venta_cliente = nuevo_precio_venta
                            except ValueError:
                                print("--")
                                print("Error: Ingrese el valor correctamente, intentelo de nuevo")
                                print("--")        
                                
                            while nuevo_precio_venta <= nuevo_precio_compra or nuevo_precio_venta<=0 and nuevo_precio_compra<0:
                                print("--")
                                print("NOTA: No puede introducir valores negativos")
                                print("NOTA: El valor de la venta debe ser mayor que el valor de la compra")
                                print("--")
                                nuevo_precio_compra = float(input("Precio de compra c/u: "))
                                nuevo_precio_venta = float(input("Precio de venta: "))
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
                    print("--")
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    print("--")
                    dni = None
                    while dni is None:
                        try:
                            dni = int(input("DNI del empleado: ")) 
                        except ValueError:
                            print("--")
                            print("Error: Ingrese el DNI correctamente, intentelo de nuevo")
                            print("--")
                            dni=None
                    print("--")
                    print("NOTA: El telefono no tiene que tener simbolo + o separacion de puntos")
                    print("--")
                    telefono = None
                    while telefono is None:
                        try:
                            telefono = int(input("Teléfono del empleado: ")) 
                        except ValueError:
                            print("--")
                            print("Error: Ingrese el telefono correctamente, intentelo de nuevo")
                            print("--")
                            telefono=None
                        
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
                    print("--")
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    print("--")
                    try:
                        dni_empleado = int(input("Inserte el DNI del empleado: "))
                    except ValueError:
                        print("Ingrese el DNI correctamente, Corroborelo y vuelva a ingresar.")
                    if disqueria.contiene_empleado(dni_empleado):
                        disqueria.eliminar_empleado(dni_empleado)
                        print("--")
                        print("Empleado dado de baja.")
                        print("--")
                        
                    else:
                        print("--")
                        print("El empleado no existe.")
                        print("--")

                elif opcion == "8": #modificar empleado
                    print("--")
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    print("--")
                    try:
                       dni_empleado = int(input("Inserte el DNI del empleado: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el DNI correctamente, Corroborelo y vuelva a ingresar")
                        print("--")
                        continue 
                    print("--")
                    print("Valores anteriores")
                    print("--")
                        
                    empleado = disqueria.buscar_empleado(dni_empleado)
                    if disqueria.contiene_empleado(dni_empleado):
                        modificar_nombre = input("¿Desea modificar el nombre del empleado? (S/N): ")
                        if modificar_nombre.lower() == 's':
                            nuevo_nombre = input("Nuevo nombre del empleado: ")
                            empleado.nombre = nuevo_nombre
                            print("--")
                            print("NOTA: El telefono no tiene que tener simbolo + o separacion de puntos")
                            print("--")
                        
                        modificar_tel = input("¿Desea modificar el telefono del empleado? (S/N): ")
                        if modificar_tel.lower() == 's':
                            nuevo_telefono= None
                            while nuevo_telefono is None:
                                try:
                                    nuevo_telefono = int(input("Nuevo telefono del empleado: "))
                                    empleado.telefono = nuevo_telefono
                                except ValueError:
                                    print("--")
                                    print("Error: Ingrese el telefono correctamente, intentelo de nuevo")
                                    print("--")
                                    nuevo_telefono=None
                        modificar_direccion = input("¿Desea modificar la dirección del empleado? (S/N): ")
                        if modificar_direccion.lower() == 's':        
                            nueva_direccion = (input("Nueva dirección del empleado: "))
                            empleado.direccion = nueva_direccion
                        
                        modificar_cargo = input("¿Desea modificar el cargo del empleado? (S/N): ")
                        if modificar_cargo.lower() == 's':
                            nuevo_cargo = input("Nuevo cargo del empleado: ")
                            empleado.cargo = nuevo_cargo
                                   
                        print("Empleado modificado con éxito.")
                    else:
                        print("El empleado no está cargado en la disquería.")


                elif opcion == "9":
                    # Buscar empleado
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    try:
                       dni_empleado = int(input("Insertar el DNI del empleado: "))
                    except ValueError:
                        print("--")
                        print("Error: Ingrese el DNI correctamente, Corroborelo y vuelva a ingresar")
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
                    print("NOTA: El ID del album no contiene ninguna letra o caracter especial")
                    id_album= None
                    while id_album is None:
                        try:
                             id_album = int(input("ID del álbum a vender: "))
                        except ValueError:
                            print("--")
                            print("Error: Ingrese el ID correctamente, intentelo de nuevo")
                            print("--")
                            id_album=None
                    cantidad= None
                    while cantidad is None:
                        try:
                            cantidad = int(input("Cantidad de unidades a vender: "))
                        except ValueError:
                            print("--")
                            print("Ingrese los valores correctos")
                            print("--")
                            cantidad=None
                    while cantidad <=0:
                        print("NOTA: La cantidad de unidades a vender debe ser mayor a 0 ")
                        cantidad = int(input("Cantidad de unidades a vender: "))
                    print("NOTA: El DNI no tiene que estar separado de puntos ")
                    dni_empleado= None
                    while dni_empleado is None:
                        try:
                            dni_empleado = int(input("DNI del empleado que realiza la venta: "))
                        except ValueError:
                            print("--")
                            print("Error: Ingrese El DNI correctamente") 
                            print("--")
                            dni_empleado=None
                           
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