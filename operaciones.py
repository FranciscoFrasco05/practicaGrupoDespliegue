# operaciones.py

def sumar(a, b):
    # Verificar que ambos parámetros sean int o float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser de tipo int o float")

def restar(a, b):
    # Verificar que ambos parámetros sean int o float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser de tipo int o float")

def multiplicar(a, b):
    # Verificar que ambos parámetros sean int o float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        resultado = 0
        for _ in range(int(abs(b))):  # Repetir la suma abs(b) veces
            resultado += a
        if b < 0:
            resultado = -resultado
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser de tipo int o float")
def dividir(a, b):
    # Verificar que ambos parámetros sean int o float
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos parámetros deben ser de tipo int o float")
    
    # Verificar que el divisor no sea cero
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    
    resultado = 0
    dividendo = abs(a)
    divisor = abs(b)
    
    while dividendo >= divisor:
        dividendo -= divisor
        resultado += 1

    # Ajustar el signo del resultado
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        resultado = -resultado
    
    return resultado
    
    
def factorial_recursivo(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    Args:
        n (int): Número para calcular el factorial.
        
    Returns:
        int: Factorial del número, o un mensaje de error si no es válido.
    """
    if not isinstance(n, int) or n < 0:
        return "Error: El número debe ser un entero no negativo"
    
    def calcular_factorial(m):
        if m <= 1:
            return 1
        return m * calcular_factorial(m - 1)
    
    return calcular_factorial(n)

def factorial_iterativo(n):
    """
    Calcula el factorial de un número de forma iterativa.
   
    Args:
        n (int): Número para calcular el factorial.
       
    Returns:
        int: Factorial del número, o None si el número no es un entero positivo.
    """
    if not isinstance(n, int) or n < 0:
        return "Error: El número debe ser un entero no negativo"
   
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fibonacci(n):
    if not isinstance(n, int):
        return "Error: El valor debe ser un número entero."
    if n < 0:
        return "Error: El número debe ser mayor o igual a cero."
    
    # Caso base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Cálculo iterativo
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
