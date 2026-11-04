
correctas = int(input("Introduce las respuestas correctas: "))
incorrectas = int(input("Introduce las respuestas incorrectas: "))
en_blanco = int(input("Introduce las respuestas en blanco: "))

nota = correctas * 5 - incorrectas * 1 + en_blanco * 0

print("La nota final es", nota)