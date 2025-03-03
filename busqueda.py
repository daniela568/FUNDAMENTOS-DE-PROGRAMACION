def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz."


# Matriz 3x3 de ejemplo
matriz = [
    [10, 25, 37],
    [45, 50, 62],
    [78, 84, 91]
]

# Valor a buscar
valor_buscado = int(input("Ingresa el valor a buscar: "))

# Búsqueda en la matriz
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar resultado
print(resultado)
