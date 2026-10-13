#Array 
#from array import 
import array as arr

# Creacion de un arreglo 
# i: Entero con nsugno 
# I: Entero sin signo 
# f: Numero decimal
# d:Numero decimal doble
# u:Caracteres unicode
my_array = arr.array('i',[10,22,300,3,740,55,80,700,654,34])

# Interacion automatica
# for num in my_array:
  #  print(num)

# Acceso individual de elementos 
# print(my_array[0]) # Primer elemento
# print(my_array[1]) # Segundo elemento
# print(my_array[1]) # Tercer elemnto

# Tamaño de un arreglo
# Lenght
print(len(my_array))

# Interar por indice 
# for i in range(len(my_array)):
#     #print(f"Elemento {i+1}: {my_array[i]}")
#     if my_array[i] % 2==0:
#         print (f"Elementos Num {i+1}:{my_array[i]}")

# Busqueda de un elemnto 
num_to_search = 200

# Modificando un valor 
# backet notation
my_array[7]=200

try:
    print(f"Localizado {num_to_search}: {my_array.index(num_to_search)}")
except:
    print("⚠️ Numero no encontrado!!!") 

