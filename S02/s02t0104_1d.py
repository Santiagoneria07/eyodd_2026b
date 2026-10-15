# Eliminación
# Importando funcion Array
from array import array as arr

# Importando una fincion de otro archivo
# como arr
from s02t0102_1d import print_array

# Importando una una funcion de otro
#archivo
my_array = arr('i',[2,10,15,20,10])

print ("--- ANTES DE LA ELIMINACION ---")
print_array(my_array)

# Eliminacion
try:
    my_array.remove(10)
except:
    print(f"no se encuentra e el arreglo")
while 
print ("--- DESPUES DE LA ELIMINACION  ---")
print_array(my_array)


