# Reto_6

1. Add the required exceptions in the Reto 1 code assigments.
2. In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

## Reto 1 Remastered

### Es Primo
se añade la excepcion de valueError que sucede cuanto se da un tipo de dato diferente a int o float, ademas de una excepcion general para problemas no indentificados o inesperados
``` python
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
```

### Mismos Caracteres
se añade la excepcione de valueError que sucede cuando la longitud de la lista es menor a dos, ademas de un Exception para errores no identificados o inesperados
```python
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
```

### Operaciones
Se añade la excepcion ZeroDivisionError que pasa cuando se ejecuta la division y el denominador es cero, ademas de un ValueError que sucede cuando no se escoge un operador disponible.
```python
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
```

### Palindromo
En este codigo solo se añadio una excepcion de tipo Exception ya que no se detectaron posibles errores, entonces se añade esta excepcion para errores no identificados o inesperados.
```python
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
```

### Suma Consecutiva
Se añade una excepcion ValueError que sucede cuando la longitud de la lista es menor de 2, ademas de un Exception para problemas no identificados o inesperados.
```python
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
```

## Shape
Se añadieron difentes excepciones como ValueError y TypeError las cuales se utilizan mas que todo para verificar el tipo de dato dado en cada clase ademas de su valor, ademas se añadio la excepcion Exception para problemas no identificados o inesperados.

```python
import math

class Point:
    def __init__(self, x=0, y=0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numeric values.") # verifica que los numeros dados sean numericos
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a numeric value.") # verifica que el numero dado sea numerico
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a numeric value.") # verifica que el numero dado sea numerico
        self._y = value

    def compute_distance(self, other):
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point instance.") # verifica que el argumento sea un objeto Point
        return math.sqrt((self._x - other.get_x()) ** 2 + (self._y - other.get_y()) ** 2)

class Line:
    def __init__(self, start, end):
        if not all(isinstance(point, Point) for point in (start, end)):
            raise TypeError("Start and end must be instances of Point.") # verifica que los argumentos sean un objeto Point
        self._start = start
        self._end = end

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def length(self):
        return self._start.compute_distance(self._end)

class Shape:
    def __init__(self, vertices):
        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError("Vertices must be instances of Point.") # verifica que el argumento sea un objeto Point
        self._vertices = vertices
        self._edges = [Line(vertices[i], vertices[(i + 1) % len(vertices)]) for i in range(len(vertices))]

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def compute_area(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def compute_perimeter(self):
        return sum(edge.length() for edge in self._edges)

class Rectangle(Shape):
    def __init__(self, bottom_left, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Width and height must be numeric values.") # verifica que los numeros dados sean numericos
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive values.") # verifica que los numeros dados sean numericos y positivos
        vertices = [
            bottom_left,
            Point(bottom_left.get_x() + width, bottom_left.get_y()),
            Point(bottom_left.get_x() + width, bottom_left.get_y() + height),
            Point(bottom_left.get_x(), bottom_left.get_y() + height)
        ]
        super().__init__(vertices)
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a numeric value.") # verifica que el numero dado sea numerico
        if value <= 0:
            raise ValueError("Width must be positive.") # verifica que el numero dado sea numerico y positivo
        self._width = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Height must be a numeric value.") # verifica que el numero dado sea numerico
        if value <= 0:
            raise ValueError("Height must be positive.") # verifica que el numero dado sea numerico y positivo
        self._height = value

    def compute_area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, bottom_left, side_length):
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise TypeError("Side length must be a positive numeric value.") # verifica que el numero dado sea numerico o positivo
        super().__init__(bottom_left, side_length, side_length)

class Triangle(Shape):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("A triangle must have exactly 3 vertices.") # verifica que el objeto Triangle tenga 3 vertices
        super().__init__(vertices)

    def compute_area(self):
        a, b, c = self._vertices
        return abs(a.get_x() * (b.get_y() - c.get_y()) + b.get_x() * (c.get_y() - a.get_y()) + c.get_x() * (a.get_y() - b.get_y())) / 2

    def get_triangle_type(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        if ab + bc <= ca or bc + ca <= ab or ca + ab <= bc:
            raise ValueError("The vertices do not form a valid triangle.") # verifica que con los vertices dados se pueda formar la figura
        return ab, bc, ca

class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_isosceles(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return math.isclose(ab, bc) or math.isclose(bc, ca) or math.isclose(ca, ab)

class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_equilateral(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return math.isclose(ab, bc) and math.isclose(bc, ca)

class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def is_scalene(self):
        a, b, c = self._vertices
        ab = a.compute_distance(b)
        bc = b.compute_distance(c)
        ca = c.compute_distance(a)
        return not (math.isclose(ab, bc) or math.isclose(bc, ca) or math.isclose(ca, ab))

class TriRectangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)

    def is_right_triangle(self):
        a, b, c = self._vertices
        sides = [a.compute_distance(b), b.compute_distance(c), c.compute_distance(a)]
        sides.sort()
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

if __name__ == "__main__":
    try:
        p1 = Point(0, 0)
        p2 = Point(2, 0)
        p3 = Point(1, 2)

        rect = Rectangle(p1, 4, 3)
        print(f"Rectangle Area: {rect.compute_area()}")
        print(f"Rectangle Perimeter: {rect.compute_perimeter()}")

        square = Square(p1, 4)
        print(f"Square Area: {square.compute_area()}")
        print(f"Square Perimeter: {square.compute_perimeter()}")

        triangle = Triangle([p1, p2, p3])
        print(f"Triangle Area: {triangle.compute_area()}")

        tri_equilateral = Equilateral([p1, p2, p3])
        print(f"Is Equilateral?: {tri_equilateral.is_equilateral()}")

        tri_isosceles = Isosceles([p1, p2, p3])
        print(f"Is Isosceles?: {tri_isosceles.is_isosceles()}")

        tri_scalene = Scalene([p1, p2, p3])
        print(f"Is Scalene?: {tri_scalene.is_scalene()}")

        tri_rectangle = TriRectangle([p1, p2, p3])
        print("Is Right Triangle:", tri_rectangle.is_right_triangle())

    except TypeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

```
