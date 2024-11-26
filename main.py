# main.py
from menu import mostrar_menu, ejecutar_operacion

while True:
    opcion = mostrar_menu()
    resultado = ejecutar_operacion(opcion)
    if resultado == "Salir":
        print("Saliendo del programa...")
        break
    print(f"Resultado: {resultado}")