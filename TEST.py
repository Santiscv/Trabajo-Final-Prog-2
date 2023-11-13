from disqueria import *


# --- TESTS CLASE DISQUERIA ---
disqueria = Disqueria()


#Test crear empleado y contiene empleado
empleado = Empleados("Matias",30331261,4804828,"Av Siempreviva 1234","vendedor")
disqueria.alta_nuevo_empleado(empleado)
assert disqueria.contiene_empleado(30331261) == True


# Test buscar empleado
test_buscar = disqueria.buscar_empleado2(30331261)
assert test_buscar.dni == 30331261


# Test crear album y contiene album
album = Album("1","Gaia","Mago de Oz","Metal","cd",20,30.0,40.0)
disqueria.alta_nuevo_album(album)
print(disqueria.contiene_album("1"))


# Test buscar album
album = disqueria.buscar_album2("1")
assert album.id == "1"


# Test baja empleado
disqueria.eliminar_empleado(30331261)
assert disqueria.contiene_empleado(30331261) == False


# Test baja album
disqueria.eliminar_album("1")
assert disqueria.contiene_album("1") == False


# --- TEST CLASE EMPLEADO ---
empleado = Empleados("Matias",30331261,4804828,"Av Siempreviva 1234","vendedor")
assert (empleado == empleado) == True
empleado2 = Empleados("Pedro",40331261,5804828,"Av Siempreviva 2234","encargado")
assert (empleado == empleado2) == False
print(empleado < empleado2)
print(empleado <= empleado2)
print(empleado != empleado2)
print(empleado > empleado2)
print(empleado >= empleado2)
