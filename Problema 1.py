import random


def buscar_extremos(arreglo, indice=0, min_valor=None, max_valor=None):
    if indice == len(arreglo):
        return min_valor, max_valor

    numero = arreglo[indice]
    if numero % 3 == 0:
        if min_valor is None or numero < min_valor:
            min_valor = numero
        if max_valor is None or numero > max_valor:
            max_valor = numero

    return buscar_extremos(arreglo, indice + 1, min_valor, max_valor)


def main():
    try:
        n = int(input("Ingresa el tamaño del arreglo: "))
    except ValueError:
        print("Debes escribir un número entero.")
        return

    if n <= 0:
        print("El tamaño debe ser mayor que cero.")
        return

    arreglo = [random.randint(10, 9999) for _ in range(n)]
    minimo, maximo = buscar_extremos(arreglo)

    print("Arreglo:", arreglo)
    if minimo is None:
        print("No hay múltiplos de 3 en el arreglo.")
        return

    promedio = (minimo + maximo) / 2
    print(f"Mínimo múltiplo de 3: {minimo}")
    print(f"Máximo múltiplo de 3: {maximo}")
    print(f"Promedio: {promedio}")


if __name__ == "__main__":
    main()