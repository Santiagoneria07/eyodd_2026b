from array import array as arr 

# Parametros de mi cuadricula 
rows = 8
columns = 2 * rows - 1

# Creando el grid 2D
matrix = []
# Contruyendo el grid
for _ in range(rows):
    new_row = arr('i',[0] * columns)
    matrix.append(new_row)

# Validando la construccion del Grid
print (f"Cantida de filas: {len(matrix)}")
print (f"Cantidad de columnas: {len(matrix[0])} ")

for row in matrix:
    print(list(row))

