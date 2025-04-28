def mostrar_tabla_multiplicar():
    numero = int(input("Escribe un número para mostrar su tabla de multiplicar: "))

    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = i * numero
        print(f"{numero} x {i} = {resultado}")

def main():
    while True:
        mostrar_tabla_multiplicar()

        repetir = input("\n¿Deseas ver otra tabla? (s/n): ").lower()
        if repetir != 's':
            print(" Programa finalizado.")
            break

main()
