def primo(n):
    # Verifica que el numero sea primo o no
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [num for num in lista if primo(num)]

try: 
    numeros = input("Introduce una lista de números separados por un espacio: ")
    numeros == int
    lista_numeros = [int(float(x)) for x in numeros.split()]

    print("Números primos:", filtrar_primos(lista_numeros))

except ValueError as e:
    print(f"Tipo de dato invalido, por favor ingrese un numero")

except Exception as e:
    print(f"Error: {e}")