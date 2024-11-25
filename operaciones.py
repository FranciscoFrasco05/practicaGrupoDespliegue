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
+