from random import choice, sample
from time import sleep
from os import system, name

FILAS_CARTON = 3
COLUM_CARTON = 5
TACHADO = "\U00002B55".strip()
NUM_MIN, NUM_MAX = 1, 90

def generar_numeros():
    """Genera una lista de números del 1 al 90."""
    return [int(x) for x in range(NUM_MIN,NUM_MAX+1)]

def generar_numeros_carton(numeros):
    """Selecciona aleatoriamente números para formar un cartón de bingo."""
    return sorted(sample(numeros, FILAS_CARTON * COLUM_CARTON))

def generar_carton(numeros):
    """Genera la matriz del cartón de bingo con los números seleccionados."""
    matriz_carton = [[" "] * COLUM_CARTON for _ in range(FILAS_CARTON)]
    indice = 0

    for c in range(len(matriz_carton[0])):
        for f in range(len(matriz_carton)):
            matriz_carton[f][c] = numeros[indice]
            indice += 1

    return matriz_carton

def hay_ganador(carton):
    """Comprueba si todos los números del cartón han sido tachados."""
    return all(carton[f][c] == TACHADO for c in range(len(carton[0])) for f in range(len(carton)))

def comprobar_linea(carton):
    """Verifica si hay al menos una línea completa tachada en el cartón."""
    hay_linea = False
    for fila in carton:
        if all(num == TACHADO for num in fila):
            hay_linea = True
            break

    return hay_linea

def sacar_bola(numeros):
    """Extrae aleatoriamente una bola del bombo y la elimina de la lista de disponibles."""
    bola = choice(numeros)
    numeros.remove(bola) 
    return bola

def tachar_numero(carton, num):
    """Tacha un número en el cartón si está presente."""
    for fila in range(len(carton)):
        for colum in range(len(carton[0])):
            if carton[fila][colum] == num:
                carton[fila][colum] = TACHADO
                break

def imprimir_carton(carton):
    """Imprime el cartón de bingo en pantalla."""
    for fila in range(len(carton)):
        for colum in range(len(carton[0])):
            print(f"{carton[fila][colum]}", end=" ")
        print()

def limpiar_pantalla():
    """Limpia la pantalla de manera compatible con Windows y Linux/macOS."""
    system("cls" if name == "nt" else "clear")

def jugar():
    """Función principal que maneja la lógica del juego de bingo."""
    tecla = ""
    while tecla == "":
        tecla = input("Pulse alguna tecla para empezar: ")
        if tecla == "":
            print("Intentelo de nuevo")

    numeros = generar_numeros()

    print("\nGenerando cartón aleatorio...")
    sleep(1.5)
    numeros_carton = generar_numeros_carton(numeros)
    carton = generar_carton(numeros_carton)
    bolas_sacadas, nueva_bola = "", "a"
    linea = False
    turnos = 0

    imprimir_carton(carton)
    sleep(2)
    print()
    while not hay_ganador(carton):
        input("Pulse ENTER para sacar una bola")
        print("Sacando bola....")
        sleep(1.5)
        bola = sacar_bola(numeros)

        print()

        turnos += 1
        bolas_sacadas += str(bola) + " "
        tachar_numero(carton,bola)

        print(f"Bolas sacadas del bombo: {bolas_sacadas}\n")

        if not linea:
            linea = comprobar_linea(carton)
            if linea:
                print(f"Se ha cantado línea en la bola {bola}")
                sleep(2)

        imprimir_carton(carton)

        sleep(2)
        limpiar_pantalla()

        if hay_ganador(carton):
            print(f"Enhorabuena, has hecho bingo en {turnos} turnos")
                
if __name__ == '__main__':
    print("Bienvenido al Bingo!")
    print(f"Este juego consta de un bombo con bolas que van del número {NUM_MIN} al {NUM_MAX}")
    print("Se ira sacando por cada ronda un número y se comprobará que este en su cartón")
    print("El juego se terminara cuando hayas tachado todos los numeros\n")
    decision = ""
    while decision != "s" and decision != "n":
        decision = input("¿Le gustaría jugar? (S / N): ").lower()
        if decision == "s":
            jugar()
            decision = ""
        elif decision == "n":
            print("Cerrando bingo, hasta la próxima")
        else:
            print("Opción incorrecta")
