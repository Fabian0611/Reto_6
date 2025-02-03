def mismos_caracteres(lista):
    # Se asegura que la lista tenga minimo 2 palabras
    if len(lista) < 2:
        raise ValueError("La lista debe tener minimo 2 palabras")
    
    # Devuelve una lista con las palabras que tienen los mismos caracteres
    resultado = []
    for palabra in lista:
        if sorted(palabra) == sorted(lista[0]):
            resultado.append(palabra)
    return resultado

try:
    palabras = input("Introduce una lista de palabras separadas por espacios: ")
    lista_palabras = palabras.split()

    print("Palabras con los mismos caracteres:", mismos_caracteres(lista_palabras))

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"Error: {e}")