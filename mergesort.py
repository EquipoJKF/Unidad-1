# Codigo para merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        izq = arr[:mid]
        der = arr[mid:]

        merge_sort(izq) 
        merge_sort(der)  

        i = j = k = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1
            k += 1

    while i < len(izq):
            arr[k] = izq[i]
            i += 1
            k += 1

    while j < len(der):
            arr[k] = der[j]
            j += 1
            k += 1

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

    print("Arreglo ingresado:", arr)

    merge_sort(arr) 
    print("Arreglo final:", arr)

