def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debes ingresar un número entero")
            
def etapa1():
    print("\n=== ETAPA 1: Lista unidimensional ===")
    numeros = [15, 8, 23, 4, 42, 16, 7, 31, 19, 11]
    
    print("\nElementos de la lista:")
    for i in range(len(numeros)):
        print(f"Posición {i}: {numeros[i]}")
    
    nuevo = leer_entero("\nIngrese el nuevo valor para el tercer elemento: ")
    numeros[2] = nuevo
    print("Lista modificada:", numeros)
    
    buscado = leer_entero("\nIngrese un número a buscar: ")
    if buscado in numeros:
        print(f"El número {buscado} sí existe (posición {numeros.index(buscado)}).")
    else:
        print(f"El número {buscado} no existe en la lista.")

def main():
    while True:
        print("\n=== LABORATORIO TEMA 3 ===")
        print("1. Etapa 1 - Lista unidimensional")
        print("5. Salir")
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            etapa1()
        elif opcion == "5":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")
 

main()