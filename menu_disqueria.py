from disqueria import Disqueria, Album, Empleados 

def menu():
    opcion = 0
    while opcion < 1 or opcion > 13:
        print("------ Menú Disqueria ------")
        print("(1)  Dar de alta nuevo Album")
        print("(2)  Dar de baja Album")
        print("(3)  Buscar Album")
        print("(4)  Modificar Album")     #pensar bien la logica
        print("(5)  Listar Albums")       # pensar bien la logica (creo que se usa __iter__)
        print("(6)  Dar de alta nuevo Empleado")
        print("(7)  Dar de baja Empleado")
        print("(8)  Modificar Empleado")
        print("(9)  Buscar Empleado")
        print("(10) Listar Empleados")
        print("(11) Guardar archivo")
        print("(12) Leer archivo")
        print("(13) Salir")
        print("---------------------------")
        opcion = int(input("Elija una opcion: "))
        print("---------------------------")
    return opcion

#mejorar todo esta logica en base a Disqueria, Album y Empleados

def run(disqueria):    
    opcion = 0
    while opcion != 13:    #Mientras que sea distinto de 13 =--->(salir)
        opcion = menu()
        if opcion == 1:
            id_album = input("ID del album: ")     #dar de alta un album
            nombre_album = input("Nombre del album: ")
            artista = input("Nombre del Artista: ")                     
            genero_musical = input("Genero musical: ")                         
            categoria = input("Categoria: ")                             
            stock = input("Cant de producto: ")
            precio_de_compra = float(input("Precio de compra: "))
            precio_venta_cliente = float(input("Precio de venta: "))
            album = Album(nombre_album,artista,genero_musical,categoria,stock,precio_de_compra,precio_venta_cliente)                             
#completar
            if disqueria.contiene_album(Album.nombre): 
                print("El Album ya existe.")
            else:
                disqueria.alta_nuevo_album(album)        
                print("Album Agregado")

        if opcion == 2: # dar de baja un album
            id = input("Inserte el ID del album: ")
            if disqueria.contiene_album(id):
                print("El Album no existe")
            else:
                disqueria.eliminar_album(id)
                print("Album dado de baja")

        if opcion == 3: #buscar album
            id_album = input("Inserte el ID del album: ")
            if disqueria.contiene_album(id):               #ver bien
                disqueria.buscar_album(id)                 #ver bien
            else:
                print("No se encuentra el album")

        if opcion == 4:  #modificar album
            id_album = input("Inserte el ID del album a modificar: ")
            if disqueria.contiene_album(nombre_album):
                nuevo_nombre = input("Nuevo nombre del álbum: ")
                nuevo_artista = input("Nuevo nombre del artista: ")
                nuevo_genero_musical = input("Nuevo género musical: ")
                nueva_categoria = input("Nueva categoría: ")
                nuevo_stock = input("Nueva cantidad de producto: ")
                nuevo_precio_compra = float(input("Nuevo precio de compra: "))
                nuevo_precio_venta = float(input("Nuevo precio de venta: "))
                

                album = disqueria.buscar_album(nombre_album)

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

        if opcion == 5: #listar album
           disqueria.mostrar_albumes()

        if opcion == 6: #dar de alta empleado
            nombreE= input("Nombre del empleado: ")
            dni= input("DNI del empleado: ")
            telefono= input("Telefono del empleado: ")
            direccion = input("Direccion del empleado: ")
            cargo= input("Cargo asignado: ")
            empleado = Empleados(nombreE, dni, telefono, direccion, cargo)
            
            if disqueria.contiene_empleado(empleado.dni):
                print("El empleado ya existe.")
            else:
                disqueria.alta_nuevo_empleado(empleado)
                print("Empleado dado de alta.")


        if opcion == 7: #dar de baja empleado
            dni_empleado = input("Inserte el dni del empleado: ")
            if disqueria.contiene_empleado(dni):
                disqueria.eliminare_mpleado(dni_empleado)
                print("Empleado dado de baja.")
            else:
                print("El empleado no existe.")
        
        if opcion == 8: #modificar empleado
            pass

        if opcion == 9: #buscar empleado
            dni_empleado = input("Insertar el dni del empleado: ")
            if disqueria.contiene_empleado(dni_empleado):               #ver bien
                disqueria.buscar_empleado(dni_empleado)                 #ver bien
            else:
                print("No se encuentra el empleado")

        if opcion == 10: #listar empleados
            disqueria.mostrar_empleados()

        if opcion == 11: #guardar archivo
            disqueria.guardar_archivo()

        if opcion == 12: # leer archivo
            disqueria.leer_archivo()
        print("Albums: ")          #ver bien 
        print("Elmpleados: ")      #ver bien

if __name__ == "__main__":
    disqueria = Disqueria()
    run(disqueria)