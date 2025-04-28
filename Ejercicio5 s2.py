import random

def adivina_el_numero ():
    numero_aleatorio = random.randint(1,10)
    print("¡Bienvenido al juego de adivinar el numero!")
    print("Se ha generado un numero del 1 al 10 y solo tienes tres intentos para adivinarlo.")

    intentos = 3 

    while intentos > 0 :
        try:
            intento = int(input(f"\nTienes {intentos} intentos restantes ¿Ya sabes que numero es?:"))

            if intento < 1 or intento > 10:
                print("Por favor, ingresa un número entre 1 y 10.")
                continue
            if intento == numero_aleatorio:
                print("¡Felicidades has adivindo el numero!")
                break
            elif intento < numero_aleatorio:
                print("El numero es mayor, intenta de nuevo")
            else:
                print("El numero es menor, intenta de nuevo")
            intentos -= 1

            if intentos == 0:
                print(f"No te quedan intentos, perdiste. El numero era {numero_aleatorio}")
        except ValueError:
            print("Por favor, ingresa un numero entero valido")

adivina_el_numero ()
