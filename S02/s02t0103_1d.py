# Importando funcion Array
from array import array as arr

# Importando una fincion de otro archivo
# como arr
from s02t0102_1d import print_array

# Importando una una funcion de otro
#archivo
my_array = arr('i',[2,10,15,20])

print ("--- ANTES DE LA INSERCION --")
print_array(my_array)

# insercion
my_array.insert(1,90)
print ("--- DESPUES DE LA INSERCION --")
print_array(my_array)

print ("--- DESPUES DE LA APPEND ---")
my_array.append(1000)
print_array(my_array)

print("--- SIMULAR UN APPEND CON INSERT ---")
my_array.insert(len(my_array),90000)
print_array(my_array)
