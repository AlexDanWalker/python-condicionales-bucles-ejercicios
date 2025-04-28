def cuenta_regresiva():
    while True:
        try:
            numero = int(input("Escribe un número entero positivo: "))
            if numero > 0:
                break
            else:
                print(" El número debe ser positivo. Intenta de nuevo.")
        except ValueError:
            print(" Entrada no válida, debes ingresar un número entero positivo.")
    
    print(f"\nCuenta regresiva desde {numero}:")
    while numero >= 0:
        print(numero)
        numero -= 1

cuenta_regresiva()