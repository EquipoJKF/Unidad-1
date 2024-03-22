#Codigo para quick sort 

def partition(arr, inicio, fin):
    pivote = arr[fin]
    i = inicio - 1
    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1

def quick_sort_recursivo(arr, inicio, fin):
    if inicio < fin:
        pi = partition(arr, inicio, fin)
        quick_sort_recursivo(arr, inicio, pi - 1)
        quick_sort_recursivo(arr, pi + 1, fin)

def quick_sort(arr):
    quick_sort_recursivo(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    arr = []
    print("Ingrese los 10 numeros para su arreglo:")
    for _ in range(10):
        while True:
            try:
                numero = int(input("Ingresa un numero: "))
                arr.append(numero)
                break
            except ValueError:
                print("ERROR")

    print("Arreglo inicial:", arr)

    quick_sort(arr)
    print("Arreglo final:", arr)
