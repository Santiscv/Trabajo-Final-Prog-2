import pickle #libreria para guardar y recuperar informacion
from Arbol_binario import ArbolBinarioBusqueda                           #abb = Arbol binario de busqueda.

class Socio():
    def __init__(self,dni,nombre,telefono,domicilio):
        self.dni =dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.dni<other.dni
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.dni<=other.dni
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.dni==other.dni
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.dni!=other.dni
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.dni>other.dni
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.dni>=other.dni

    def __str__(self):
        return "DNI: {0}\nNombre: {1}\nTelefono: {2}\nDomicilio: {3}\n" \
            .format(self.dni,self.nombre,self.telefono,self.domicilio)

class Pelicula():
    def __init__(self,titulo,genero,anio):
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.alquilada = None
    
    def __str__(self):
        return "Titulo: {0}\nGenero: {1}\nAño: {2}\nAlquilada: {3}" \
            .format(self.titulo,self.genero,self.anio,self.alquilada)
        #return f"Titulo: {self.titulo}\nGenero: {self.genero}\nAño: {self.anio}\nAlquilada: {self.alquilada}"

    def esta_alquilada(self):
        return self.alquilada != None
    
    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.titulo<other.titulo
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.titulo<=other.titulo
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.titulo==other.titulo
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.titulo!=other.titulo
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.titulo>other.titulo
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.titulo>=other.titulo

class Videoclub:
    def __init__(self):
        self.socios = ArbolBinarioBusqueda()
        self.peliculas = []

    def contiene_socio(self,dni)->bool:
        return dni in self.socios
    
    def buscar_socio(self,dni)->"Socio":
        if dni in self.socios:
            return self.socios[dni]
        else:
            return None
        
    def alta_nuevo_socio(self,socio):
        self.socios[socio.dni] = socio
        
    def baja_socio(self,dni):
        self.socios.eliminar(dni)
    
    def mostrar_socios(self):
        for socio in self.socios:
            print (socio)
    
    def contiene_pelicula(self,titulo):
        esta = False
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                esta = True
        return esta
    def buscar_pelicula(self,titulo)->"Pelicula":
        devolver = None
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                devolver = pelicula
        return devolver
    def alta_nueva_pelicula(self,pelicula)->None:
        self.peliculas.append(pelicula)
        
    def baja_pelicula(self,titulo)->None:
        pelicula = self.buscar_pelicula(titulo)
        self.peliculas.remove(pelicula)
        
    def alquilar_pelicula(self,titulo,dni):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == None:
                pelicula.alquilada = dni
                
    def devolver_pelicula(self,titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada != None:
                pelicula.alquilada = None
         
    def guardar_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo,'rb')
        video = pickle.load(pickle_file)
        self.socios = video.socios
        self.peliculas = video.peliculas
        pickle_file.close()

class Disqueria:
    def __init__(self):
        self.album = ArbolBinarioBusqueda()
        self.empleado = ArbolBinarioBusqueda()


class Album:
    def __init__(self, nombre_album, artista, genero_musical, categoria, stock):
        self.nombre = nombre_album
        self.artista = artista
        self.genero_musical = genero_musical
        self.categoria = categoria
        self.stock = stock
        self.precio_compra_tienda = 0
        self.dinero_en_caja = 0
        self.precio_venta_cliente = 0

        
class Empleados:
    def __init__(self, nombre, dni, telefono, direccion, cargo, dinero_aportado):
        self.nombre = nombre
        self.dni = dni 
        self.telefono = telefono
        self.direccion = direccion
        self.cargo = cargo
        self:dinero_aportado = 0     








