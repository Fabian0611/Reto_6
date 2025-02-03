def palindromo(palabra) -> str:
    # Pone toda la palabra en minusculas
    palabra = palabra.lower()

    # Ciclo para verificar si la palabra es un palindromo
    for i in range(len(palabra) // 2):
        if palabra[i] == palabra[-(i + 1)]:
            return True
        else:
            return False


try:
    palabra = (input("Ingrese una palabra:"))
    if palindromo(palabra):
        print(f"{palabra} es un palindromo")
    else:
        print(f"{palabra} no es un palindromo")

except Exception as e:
    print(f"Error: {e}")