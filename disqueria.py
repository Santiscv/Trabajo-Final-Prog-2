import pickle #libreria para guardar y recuperar informacion
from Arbol_binario import ArbolBinarioBusqueda #abb = Arbol binario de busqueda.

class Disqueria:
    def __init__(self):
        self.arbol_album = ArbolBinarioBusqueda()
        self.arbol_empleado = ArbolBinarioBusqueda()
    
    def contiene_album(self,id)->bool: #igual
        return id in self.arbol_album
    
    def buscar_album(self,id)->"Album": #igual
        if id in self.arbol_album:
            return self.arbol_album[id]
        else:
            return None
        
    def alta_nuevo_album(self,album):
        self.arbol_album[album.id] = album #igual
        
    def eliminar_album(self, id): #igual
        self.arbol_album.eliminar(id)
    
    
    def mostrar_albumes(self):
        self.arbol_album.inorden() #provisorio
            
            #probar
    def modificar_album(self, id,nuevo_nombre, nuevo_artista, nuevo_genero, nueva_categoria, nuevo_stock):    
        if self.arbol_album[id] == self.arbol_album(id): 
         self.arbol_album.nombre = nuevo_nombre
         self.arbol_album.artista = nuevo_artista
         self.arbol_album.genero = nuevo_genero
         self.arbol_album.categoria = nueva_categoria
         self.arbol_album.stock = nuevo_stock
        
    ############ empleado ##########
    
    
    def alta_nuevo_empleado(self, empleado)->None: #igual
        self.arbol_empleado[empleado.dni] = empleado
        
    
    def eliminar_empleado(self,dni)->None: 
        self.arbol_empleado.eliminar(dni)   
                    
    def contiene_empleado(self,dni)->bool:
        return dni in self.arbol_empleado
    
    def buscar_empleado(self, dni)->"Empleados": #igual
        if dni in self.arbol_empleado:
            empleado= self.arbol_empleado[dni]
            print(empleado)
            return empleado
        else:
            return None
    
    
    def mostrar_empleados(self):
        self.arbol_empleado.inorden() #provisorio
    
        
    def modificar_empleado(self, dni, nuevo_nombre,nuevo_telefono, nueva_direccion, nuevo_cargo, nuevo_dinero_aportado):
        if self.arbol_empleado[dni] == self.arbol_empleado.buscar_empleado(dni):
            self.arbol_empleado.nombre = nuevo_nombre
            self.arbol_empleado.telefono = nuevo_telefono
            self.arbol_empleado.direccion = nueva_direccion
            self.arbol_empleado.cargo = nuevo_cargo
            self.arbol_empleado.dinero_aportado = nuevo_dinero_aportado

         
    def guardar_archivo(self,archivo="disqueria.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="disqueria.pickle"):
        pickle_file = open(archivo,'rb')
        disqueria = pickle.load(pickle_file)
        self.albumes = disqueria.albumes
        self.empleados = disqueria.empleados
        pickle_file.close()

class Album:
    def __init__(self, id,nombre_album, artista, genero_musical, categoria, stock, precio_compra, precio_venta):
        self.id = id
        self.nombre = nombre_album
        self.artista = artista
        self.genero_musical = genero_musical
        self.categoria = categoria
        self.stock = stock
        self.precio_compra_tienda = precio_compra
        self.precio_venta_cliente = precio_venta
        self.dinero_en_caja = 0

    def __lt__(self, other): # x<y llama x.__lt__(y)
        return self.nombre<other.nombre
    def __le__(self, other): # x<=y llama x.__le__(y)
        return self.nombre<=other.nombre
    def __eq__(self, other): # x==y llama x.__eq__(y)
        return self.nombre==other.nombre
    def __ne__(self, other): # x!=y llama x.__ne__(y)
        return self.nombre!=other.nombre
    def __gt__(self, other): # x>y llama x.__gt__(y)
        return self.nombre>other.nombre
    def __ge__(self, other): # x>=y llama x.__ge__(y)
        return self.nombre>=other.nombre
          
        

    def __str__(self):
        return "Album: {0}\n: {1}\Artista: {2}\Genero Musical: {3}\n Categoria: {4}\n: {5}\Stock: {6}\Precio para la tienda: {7}\n Precio para el cliente: {8}\n: {9}\Dinero en caja:\n" \
            .format(self.nombre,self.artista,self.genero_musical,self.categoria,  self.stock, self.precio_compra_tienda,self.precio_venta_cliente,self.dinero_en_caja)          
            
            
class Empleados:
    def __init__(self, nombre, dni, telefono, direccion, cargo):
        self.nombre = nombre
        self.dni = dni 
        self.telefono = telefono
        self.direccion = direccion
        self.cargo = cargo
        self.dinero_aportado = 0     

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
        return "nombre: {0}\DNI: {1}\Telefono: {2}\Direccion: {3}\Cargo: {4}\Dinero aportado: {5}" \
            .format(self.nombre, self.dni, self.telefono,self.direccion,self.cargo, self.dinero_aportado)



