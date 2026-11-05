"""
Generators 

Los generadoes son funcuines que pueden 
pausar su ejecucion

Cuando se invoca una funcion generadora 
devuelve un objeto generador (aka iterador)

el codigo de la funcion no se ejcuta 
inmediato, solo se compila 

La funcion de ejecuta inicamente cuando
iteras sobre el generador  

"""

def my_generators():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4
    yield 1
    yield 2
    yield 3
    yield 4

# Se invoca funcio generadora 
my_iterator = my_generators ()

# Se itera manualmente sobre el generador 
# print(next(my_iterator))# Imprime 1
# print(next(my_iterator))# Imprime 2
# print(next(my_iterator))# Imprime 3
# print(next(my_iterator))# Imprime 4
# print(next(my_iterator))# Imprime ?

# Los iteradores se pueden iterar con un for 
for value in my_iterator:
    print (value)