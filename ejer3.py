# Autor: Alfonso Luque Sanchez
# Ejercicio 3 - Arrays con numpy
"""
Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy. El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.
"""
import numpy as np

# Generar 20 números enteros aleatorios entre 0 y 100
numbers = np.random.randint(0, 101, size=20)
print("Números generados:")
print(numbers)

pares = numbers[numbers % 2 == 0]
impares = numbers[numbers % 2 != 0]

ordenados = np.concatenate((pares, impares))

print("Array original:")
print(numbers)
print("Array con pares primero e impares después:")
print(ordenados)