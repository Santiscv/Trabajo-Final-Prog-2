from disqueria import Socio, Pelicula, Videoclub

def menu():
    opcion = 0
    while opcion < 1 or opcion > 9:
        print("--")
        print("(1) Dar de alta nuevo socio")
        print("(2) Dar de baja socio")
        print("(3) Dar de alta nueva pelicula")
        print("(4) Dar de baja pelicula")
        print("(5) Alquilar película")
        print("(6) Devolver película")
        print("(7) Guardar archivo")
        print("(8) Leer archivo")
        print("(9) Salir")
        # consultar pelicula - me devuelve la informacion de la pelicula
        print("--")
        opcion = int(input("Elija una opcion: "))
        print("--")
    return opcion

def run(videoclub):
    opcion = 0
    while opcion != 9:
        opcion = menu()
        if opcion == 1:
            nombre = input("Nombre: ")
            dni = input("Dni: ")
            telefono = input("Telefono: ")
            dire = input("Dirección: ")
            socio = Socio(dni,nombre,telefono,dire)
            if videoclub.contiene_socio(socio.dni):
                print("El socio ya existe")
            else:
                videoclub.alta_nuevo_socio(socio)
                print("Socio Agregado")
        if opcion == 2:
            dni = input("Dni:")
            if videoclub.contiene_socio(dni):
                print("El socio no existe")
            else:
                videoclub.baja_socio(socio)
                print("Socio dado de baja")
        if opcion == 3:
            titulo = input("Titulo: ")
            genero = input("Genero: ")
            anio = input("Anio: ")
            peli = Pelicula(titulo,genero,anio)
            if videoclub.contiene_pelicula(peli.titulo):
                print("La peli ya existe")
            else:
                videoclub.alta_nueva_pelicula(peli)
                print("Pelicula agregada")
        if opcion == 4:
            dni = input("Titulo:")
            if videoclub.contiene_pelicula(dni):
                print("La pelicula no existe")
            else:
                videoclub.baja_pelicula(socio)
                print("Pelicula ha sido dada de baja")
        if opcion == 5:
            titulo = input("Titulo: ")
            dni = input("DNI socio: ")
            if videoclub.contiene_pelicula() and videoclub.contiene_socio():
                videoclub.alquilar_pelicula(titulo,dni)
            else:
                print("No se pudo alquilar la pelicula")
        if opcion == 6:
            titulo = input("Titulo: ")
            if not videoclub.contiene_pelicula(titulo):
                print("La pelicula no existe")
            else:
                videoclub.devolver_pelicula(titulo)
                print("Pelicula ha sido devuelta")
        if opcion == 7:
            videoclub.guardar_archivo()
        if opcion == 8:
            videoclub.leer_archivo()
        print("Socios: ", len(videoclub.socios))
        print("Peliculas: ", len(videoclub.peliculas))

if __name__ == "__main__":
    videoclub = Videoclub()
    run(videoclub)