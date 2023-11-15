import pickle
from Arbol_binario import ArbolBinarioBusqueda

class Disqueria:
    def __init__(self):
        self.arbol_album = ArbolBinarioBusqueda()
        self.arbol_empleado = ArbolBinarioBusqueda()
        self.presupuesto_disqueria = 10000

    def imprimir_presupuesto(disqueria):
        print(disqueria)
    def __str__(self):
        return "Presupuesto en caja: {0}" \
            .format(self.presupuesto_disqueria)    

    def venta_album(self, id_album, cantidad, dni_empleado):
        album = self.buscar_album2(id_album)
        empleado = self.buscar_empleado2(dni_empleado)

        if album and empleado and cantidad > 0 and album.stock >= cantidad:
            # Realizar la venta
            precio_venta_total = album.precio_venta_cliente * cantidad

            # Actualizar empleado
            empleado.dinero_aportado += precio_venta_total

            # Actualizar album
            album.dinero_en_caja += precio_venta_total
            album.stock -= cantidad
            
            self.presupuesto_disqueria += precio_venta_total
     
    def __len__(self):
        return len(self.arbol_album)
    
    def contiene_album(self, id) -> bool:
        return id in self.arbol_album
    
    def buscar_album(self, id) -> "Album":
        if id in self.arbol_album:
            album = self.arbol_album[id]
            print(album)
            return album
        else:
            return None
        
    def buscar_album2(self, id) -> "Album":
        if self.arbol_album.obtener(id) != None:
            album = self.arbol_album.obtener(id)
            return album
        else:
            return None
        
    def alta_nuevo_album(self, album):
        self.arbol_album[album.id] = album
        
    def eliminar_album(self, id):
        self.arbol_album.eliminar(id)
    
    def mostrar_albumes(self):
        self.arbol_album.EnOrden(self.arbol_album.raiz)
    
    def modificar_album(self, id, nuevo_nombre, nuevo_artista, nuevo_genero, nueva_categoria, nuevo_stock):
        album_a_modificar = self.buscar_album2(id)
        if album_a_modificar is not None:
            album_a_modificar.nombre = nuevo_nombre
            album_a_modificar.artista = nuevo_artista
            album_a_modificar.genero = nuevo_genero
            album_a_modificar.categoria = nueva_categoria
            album_a_modificar.stock = nuevo_stock
        else:
            print("No se encontró el álbum.")

    def __len_empleado__(self):
        return len(self.arbol_empleado)

    def alta_nuevo_empleado(self, empleado) -> None:
        self.arbol_empleado[empleado.dni] = empleado

    def eliminar_empleado(self, dni) -> None:
        self.arbol_empleado.eliminar(dni)

    def contiene_empleado(self, dni) -> bool:
        return dni in self.arbol_empleado

    def buscar_empleado(self, dni) -> "Empleados":
        if dni in self.arbol_empleado:
            empleado = self.arbol_empleado[dni]
            print(empleado)
            return empleado
        else:
            return None

    def buscar_empleado2(self, dni) -> "Empleados":
        if dni in self.arbol_empleado:
            empleado = self.arbol_empleado.obtener(dni)
            return empleado
        else:
            return None

    def mostrar_empleados(self):
        self.arbol_empleado.EnOrden_empleado(self.arbol_empleado.raiz)

    def modificar_empleado(self, dni, nuevo_nombre, nuevo_telefono, nueva_direccion, nuevo_cargo, nuevo_dinero_aportado):
        empleado_a_modificar = self.buscar_empleado2(dni)
        if empleado_a_modificar is not None:
            empleado_a_modificar.nombre = nuevo_nombre
            empleado_a_modificar.telefono = nuevo_telefono
            empleado_a_modificar.direccion = nueva_direccion
            empleado_a_modificar.cargo = nuevo_cargo
            empleado_a_modificar.dinero_aportado = nuevo_dinero_aportado
         
    def guardar_archivo(self, archivo="disqueria.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self, archivo="disqueria.pickle"):
        pickle_file = open(archivo, 'rb')
        disqueria = pickle.load(pickle_file)
        self.arbol_album = disqueria.arbol_album
        self.arbol_empleado = disqueria.arbol_empleado
        pickle_file.close()

class Album:
    def __init__(self, id, nombre_album, artista, genero_musical, categoria, stock, precio_compra, precio_venta):
        self.id = id
        self.nombre = nombre_album
        self.artista = artista
        self.genero_musical = genero_musical
        self.categoria = categoria
        self.stock = stock
        self.precio_compra_tienda = precio_compra
        self.precio_venta_cliente = precio_venta
        self.dinero_en_caja = precio_venta - precio_compra

    def _lt_(self, other):
        if other is None:
            return False
        return self.nombre < other.nombre
    
    def _le_(self, other):
        if other is None:
            return False
        return self.nombre <= other.nombre
    
    def _eq_(self, other):
        if other is None:
            return False
        return self.nombre == other.nombre
    
    def _ne_(self, other):
        if other is None:
            return True
        return self.nombre != other.nombre
    
    def _gt_(self, other):
        if other is None:
            return True
        return self.nombre > other.nombre

    def _ge_(self, other):
        if other is None:
            return True
        return self.nombre >= other.nombre

    def __str__(self):
        return "ID: {0}\nAlbum: {1}\nArtista: {2}\nGenero Musical: {3}\nCategoria:  {4}\nStock:  {5}\nPrecio para la tienda: {6}\nPrecio para el cliente: {7}\nDinero beneficio: {8}" \
            .format(self.id, self.nombre, self.artista, self.genero_musical, self.categoria, self.stock, self.precio_compra_tienda, self.precio_venta_cliente, self.dinero_en_caja)          

class Empleados:
    def __init__(self, nombre, dni, telefono, direccion, cargo):
        self.nombre = nombre
        self.dni = dni 
        self.telefono = telefono
        self.direccion = direccion
        self.cargo = cargo
        self.dinero_aportado = 0     

    def __lt__(self, other):
        return self.dni < other.dni

    def __le__(self, other):
        return self.dni <= other.dni

    def __eq__(self, other):
        return self.dni == other.dni

    def __ne__(self, other):
        return self.dni != other.dni

    def __gt__(self, other):
        return self.dni > other.dni

    def __ge__(self, other):
        return self.dni >= other.dni

    def __str__(self):
        return "Nombre: {0}\nDNI: {1}\nTelefono: {2}\nDireccion: {3}\nCargo: {4}\nDinero aportado: {5}" \
            .format(self.nombre, self.dni, self.telefono, self.direccion, self.cargo, self.dinero_aportado)
