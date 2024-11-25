# main.py
from menu import mostrar_menu, ejecutar_operacion

def main():
    while True:
        opcion = mostrar_menu()
        resultado = ejecutar_operacion(opcion)
        print(f"Resultado: {resultado}")
        if opcion == "5":
            break

if __name__ == "__main__":
    main()
