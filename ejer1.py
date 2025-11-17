# Autor: Alfonso Luque Sanchez
# Ejercicio 1
"""
Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. Carga las lista number con valores aleatorios entre 0 y 100. En la lista square se deben almacenar los cuadrados de los valores que hay en number. En la lista cube se deben almacenar los cubos de los valores que hay en number. A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.
"""

import random
number = []
square = []
cube = []

for i in range(20):
    valor = random.randint(0, 100)
    number.append(valor)

for valor in number:
    square.append(valor ** 2)
    cube.append(valor ** 3)

print("Number\tSquare\tCube")
print("-"*20)

for i in range(20):
    print(f"{number[i]:<8}{square[i]:<10}{cube[i]}")

