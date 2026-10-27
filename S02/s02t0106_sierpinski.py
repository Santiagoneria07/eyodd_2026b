from array import array as arr 

# Parametros de mi cuadricula 
rows = 10
columns = 2 * rows - 1

# Funcion para imprimer matrix
def print_matrix(input_matrix):
    for row in matrix:
        print(list(row))

# Creando el grid 2D
matrix = []
# Contruyendo el grid
for _ in range(rows):
    new_row = arr('i',[0] * columns)
    matrix.append(new_row)

# Validando la construccion del Grid
print (f"Cantida de filas: {len(matrix)}")
print (f"Cantidad de columnas: {len(matrix[0])} ")

# Calculando el centro de la primera fila 
center = columns // 2 # se hace divicion de entera 

# Estableciendo en centro en 1
matrix[0][center] = 1

print_matrix(matrix)

# Se calcula el resto de la matrix 
# Siguiendo la logica de sierpinski Gasket
for row in range(1,rows):
    for columns in range (0,columns):
        left_upper_cell=0
        right_upper_cell=0

        # Si la columna donde estamos 
        # es mayor a cero
        # despues del borde izquierdo
        if columns > 0:
            left_upper_cell = matrix[row-1][columns-1]

        # Si la columna esta in elemento antes
        # del borde derecho
        if columns < columns - 1:
            right_upper_cell = matrix[row-1][columns+1]

        # Guardo el arreglo 
        if left_upper_cell != right_upper_cell:
            matrix[row][columns] = 1
        else: 
            matrix[row][columns] = 0

print ()
print_matrix(matrix)

