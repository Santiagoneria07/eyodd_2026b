"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculará la suma del 1 al 100.
42 usando un ciclo while
"""
# importar biblioteca de tiempo
import time

#crear variables para 
#el problema 
n = 100
the_sum = 0

# Tomando el T1
timestamp_01 = time.time()

#iniciando la suma 
#100
while(n > 0):
    the_sum = the_sum + n # 100 + 99 + 98 + .. + 1
    n = n - 1

    # Tomamos el T2
timestamp_02 =time.time()

# imprimimos la solucion
print (f"La suma es {the_sum}")

# Calculando el timpo
elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
print (f"Tiempo de ejecucion: {elapsed_time} us")