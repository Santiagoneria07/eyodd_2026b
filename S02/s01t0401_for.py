"""
Escribir un programa que calculé la suma de "n" números naturales.
Por ejemplo si n=100, el programa calculará la suma del 1 al 100 
"""
#importamos biblioteca time 
import time 

#creando una marca de tiempo 
timestamp_01 = time.time()

#programa que calcula las suma 
#de los "n" números naturales 
n =100 
sum = 0

#ciclo for 
for number in range(1,n+1):
    print (str(number)+ " ")