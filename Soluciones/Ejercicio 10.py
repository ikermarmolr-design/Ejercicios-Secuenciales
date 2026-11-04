
parcial1 = float(input("Introduce la calificación del parcial 1: "))
parcial2 = float(input("Introduce la calificación del parcial 2: "))
parcial3 = float(input("Introduce la calificación del parcial 3: "))
examen = float(input("Introduce la calificación del examen final: "))
trabajo = float(input("Introduce la calificación del trabajo final: "))

promedio = (parcial1 + parcial2 + parcial3) / 3
final = promedio * 0.55 + examen * 0.30 + trabajo * 0.15

print("La calificación final es", final)