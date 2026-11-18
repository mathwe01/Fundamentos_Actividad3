def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes ingresar un número entero")
            
def main():
    while True:
        print("\n=== LABORATORIO TEMA 3 ===")
        print("5. Salir")
        opcion = input("Elija una opción: ")
        
        if opcion == "5":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")


main()