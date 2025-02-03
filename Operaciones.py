def calculadora(a, b, operador):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == '/':
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        return a/b
    else:
        raise ValueError("Operador no valido, use '+','-','*','/'")
        
try:

    a= float(input("Ingrese un numero: "))
    b= float(input("Ingrese otro numero: "))
    operador= str(input("Ingrese el signo de la operación deseada: "))

    resultado = calculadora(a, b, operador)
    print(resultado)

except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")