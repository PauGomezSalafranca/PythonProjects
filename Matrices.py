import numpy as np

#####################################################################################################
# In this part of the program we are going to perform several fundamental operations on the matrices#



# Prompt the user to enter the dimensions of the first matrix
rows_A = int(input("Ingrese el número de filas de la primera matriz: "))
cols_A = int(input("Ingrese el número de columnas de la primera matriz: "))

# Initialize the first matrix with zeros
A = np.zeros((rows_A, cols_A))

# Prompting the user to enter the elements of the first matrix
print("Ingrese los elementos de la primera matriz:")
for i in range(rows_A):
    for j in range(cols_A):
        A[i, j] = float(input(f"Elemento A[{i}][{j}]: "))

# Prompt user to enter the dimensions of the second matrix
rows_B = int(input("Ingrese el número de filas de la segunda matriz: "))
cols_B = int(input("Ingrese el número de columnas de la segunda matriz: "))

# Initialize the second matrix with zeros
B = np.zeros((rows_B, cols_B))

# Prompt user to enter the elements of the second matrix
print("Ingrese los elementos de la segunda matriz:")
for i in range(rows_B):
    for j in range(cols_B):
        B[i, j] = float(input(f"Elemento B[{i}][{j}]: "))

np.set_printoptions(precision=2, suppress=True)
# We check if we can add the matrices and if so, we add them.

if cols_A != cols_B and rows_A != rows_B:
    print("\nLas matrices no se pueden sumar ya que no tienen las mismas dimensiones")
else:
    D = A + B
    print("\nEl resultado de la suma de las matrices: ")
    print(D)


# We check if we can subtract the matrices and if so, we subtract them.

if cols_A != cols_B and rows_A != rows_B:
    print("\nLas matrices no se pueden restar ya que no tienen las mismas dimensiones")
else:
    E = A + B
    print("\nEl resultado de la resta de las matrices: ")
    print(E)


# Check if the matrices are multipliable
if cols_A != rows_B:
    print("\nNo es posible multiplicar las matrices debido a dimensiones incompatibles.")
else:
    # Perform matrix multiplication
    C = np.dot(A, B)
    print("\nEl resultado de la multiplicación es:")
    print(C)


# We check if the determinant of the second matrix is different from zero, 
# and if it is, we invert it and multiply it to the first matrix to perform a matrix division.

if cols_B != rows_B:
    print("\nLa matriz no es cuadrada por lo que no se puede realizar su determinante para invertirla")
else:
    if np.linalg.det(B) == 0:
        print("\nLa segunda matriz que has introducido no es invertible, por lo que no se puede realizar una division entre estas dos")
    else:
        
        B_inv = np.linalg.inv(B)
        F = np.dot(A,B_inv)
        print("\nEl resultado de dividir las dos matrices: ")
        print(F)


# Tensor product of matrices (No need to check, can always be performed)

print("\nEl resultado del producto tensorial de tus dos matrices: ")
print(np.kron(A,B))

#####################################################################################################