def mayor_suma_consecutiva(lista):
    # Se asegura que la lista tenga minimo 2 numeros
    if len(lista) < 2:
        raise ValueError("La lista debe tener minimo 2 numeros")
    
    # Recorre la lista para verificar la mayor suma de dos numeros consecutivos
    max_suma = float('-inf')
    for i in range(len(lista) - 1):
        suma_actual = lista[i] + lista[i + 1]
        if suma_actual > max_suma:
            max_suma = suma_actual
    return max_suma

try:
    numeros = input("Introduce una lista de números separados por espacios: ")
    lista_numeros = [int(x) for x in numeros.split()]

    # Llama a la función y muestra la mayor suma consecutiva
    print("La mayor suma entre elementos consecutivos es:", mayor_suma_consecutiva(lista_numeros))

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Error: {e}")