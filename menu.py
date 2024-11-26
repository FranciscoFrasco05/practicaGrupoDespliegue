# menu.py
from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo, factorial_recursivo, fibonacci

def mostrar_menu():
    print("Selecciona una opción:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")
    print("6 - Calcular el factorial de un número (iterativo)")
    print("7 - Calcular el factorial de un número (recursivo)")
    print("8 - Calcular el Fibonacci de un número")

    opcion = input("Introduce el número de la opción: ")
    return opcion

def ejecutar_operacion(opcion):
    try:
        if opcion == "1":
            # Sumar
            a = input("Introduce el primer valor: ")
            b = input("Introduce el segundo valor: ")
            a, b = float(a), float(b)  # Convertir a float
            return sumar(a, b)
        elif opcion == "2":
            # Restar
            a = input("Introduce el primer valor: ")
            b = input("Introduce el segundo valor: ")
            a, b = float(a), float(b)  # Convertir a float
            return restar(a, b)
        elif opcion == "3":
            # Multiplicar
            a = input("Introduce el primer valor: ")
            b = input("Introduce el segundo valor: ")
            a, b = float(a), float(b)  # Convertir a float
            return multiplicar(a, b)
        elif opcion == "4":
            # Dividir
            a = input("Introduce el primer valor: ")
            b = input("Introduce el segundo valor: ")
            a, b = float(a), float(b)  # Convertir a float
            return dividir(a, b)
        elif opcion == "5":
            return "Salir"
        elif opcion == "6":
            # Calcular factorial iterativo
            numero = int(input("Ingrese un número para calcular su factorial (iterativo): "))
            resultado = factorial_iterativo(numero)
            return f"El factorial de {numero} es: {resultado}"
        elif opcion == "7":
            # Calcular factorial recursivo
            numero = int(input("Ingrese un número para calcular su factorial (recursivo): "))
            resultado = factorial_recursivo(numero)
            return f"El factorial de {numero} es: {resultado}"
        elif opcion == 8:
            num = int(input("Introduce un número para calcular el Fibonacci: "))
            resultado = fibonacci(num)
            return f"El Fibonacci de {num} es {resultado}"
        
        else:
            return "Opción no válida"
    except ValueError:
        return "Error: Los valores deben ser numéricos (int o float)."
