# Archivo: menu.py

def mostrar_menu():
    """
    Muestra un menú de opciones por consola y solicita al usuario que seleccione una opción.
    """
    print("Menú de opciones:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")
    
    # Solicitar al usuario una opción y almacenarla
    opcion = input("Seleccione una opción (1-5): ")
    
    # Retorna la opción seleccionada como entero si es válida, o como cadena para otras entradas.
    try:
        return int(opcion)
    except ValueError:
        return opcion
