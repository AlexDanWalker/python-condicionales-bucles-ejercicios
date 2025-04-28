calificacion = float (input("Escribe la calificacion del estudiante (0 a 100) =>"))

if calificacion >= 60 and calificacion <= 100:
    print("El estudiante aprobo")

elif calificacion <= 59 and calificacion >= 0:
    print("El estudiante reprobo")
else:
    print("La calificacion ingresada no es valida")