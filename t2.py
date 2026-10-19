laberinto = [
    ["F", 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ["I", 1, 3, 1, 0, 1, 1, 1, 1],
]

ruta = []


def imprimir(m):
    for fila in m:
        print(fila)


def valor_celda(fila, col):
    if laberinto[fila][col] == "I" or laberinto[fila][col] == "F":
        return 1
    return laberinto[fila][col]


def ya_paso(fila, col):
    for celda in ruta:
        if celda[0] == fila and celda[1] == col:
            return True
    return False


def buscar_salida(fila, col, total):
    if fila < 0 or fila > 8 or col < 0 or col > 8:
        return False
    if valor_celda(fila, col) == 0 or ya_paso(fila, col):
        return False

    ruta.append([fila, col])
    total = total + valor_celda(fila, col)

    if fila == 0 and col == 0:
        if total >= 23:
            print("Puntos al llegar a F:", total)
            return True
        ruta.pop()
        return False

    if buscar_salida(fila - 1, col, total):
        return True
    if buscar_salida(fila, col + 1, total):
        return True
    if buscar_salida(fila + 1, col, total):
        return True
    if buscar_salida(fila, col - 1, total):
        return True

    ruta.pop()
    return False


print("Laberinto original:")
imprimir(laberinto)
print()

if buscar_salida(8, 0, 0):
    print("El raton si logro salir")
    camino = []
    for i in range(9):
        camino.append([0] * 9)
    for celda in ruta:
        camino[celda[0]][celda[1]] = 1
    print()
    print("Matriz del camino:")
    imprimir(camino)
else:
    print("El raton no logro salir, no llego a 23 puntos")
