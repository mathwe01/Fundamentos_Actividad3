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
        
def etapa2():
    print("\n=== ETAPA 2: Matriz 3x3 ===")
    matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            matriz[i][j] = leer_entero(f"Ingrese el valor para  ({i}, {j}): ")
    print ("\nMatriz ingresada:")
    suma = 0
    for i in range(3):
        for j in range(3):
            print(f"{matriz[i][j]:5}", end ="")
            suma += matriz[i][j]
        print()
        
    print(f"\nSuma de todos los elementos: {suma}")
    
def etapa3():
    print("\n=== ETAPA 3: Operaciones sobre una lista ===")
    lista = []
    
    while True:
        print("\n1. Insertar un elemento al final")
        print("\n2. Eliminar un elemento por posición")
        print("\n3. Buscar un valor")
        print("\n4. Mostrar la lista")
        print("\n5. Volver al menú principal")
        opcion = input("Elija una opcion: ")
        
        if opcion == "1":
            valor = leer_entero("Ingrese el valor a insertar: ")
            lista.append(valor)
            print(f"Se insertó {valor}.")
        elif opcion == "2":
            if len(lista) == 0:
                print("La lista está vacía.")
            else:
                pos = leer_entero(f"Posición a eliminar (0 a {len(lista) -1}): ")
                if 0 <= pos < len(lista):
                    eliminado = lista.pop(pos)
                    print(f"Se eliminó {eliminado}.")
                else:
                    print("Posición no válida.")
        elif opcion == "3":
            valor = leer_entero("Valor a buscar: ")
            if valor in lista:
                print(f"El valor {valor} está en la posición {lista.index(valor)}.")
            else:
                print(f"El valor {valor} no está en la lista")
        elif opcion == "4":
            print("Lista actual:", lista)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")
            
def burbuja(lista):
    datos = lista.copy()
    n = len(datos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos

def etapa4():
    print("\n=== ETAPA 4: Ordenamiento ===")
    desordenada = [64, 25, 12, 22, 11, 90, 5, 38]
    print("Lista original:", desordenada)

    print("\n-- Burbuja --")
    print("Antes: ", desordenada)
    print("Después:", burbuja(desordenada))
                    
def main():
    while True:
        print("\n=== LABORATORIO TEMA 3 ===")
        print("1. Etapa 1 - Lista unidimensional")
        print("2. Etapa 2 - Matriz 3x3")
        print("3. Etapa 3 - Operaciones sobre una lista")
        print("4. Etapa 4 - Ordenamiento")
        print("5. Salir")
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            etapa1()
        elif opcion == "2":
            etapa2()
        elif opcion == "3":
            etapa3()
        elif opcion == "4":
            etapa4()
        elif opcion == "5":
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")
 

main()