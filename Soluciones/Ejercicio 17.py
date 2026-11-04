
hh = int(input("Introduce las horas de salida: "))
mm = int(input("Introduce los minutos de salida: "))
ss = int(input("Introduce los segundos de salida: "))
t = int(input("Introduce el tiempo de viaje en segundos: "))

total = hh * 3600 + mm * 60 + ss + t

horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print("Llegará a las", horas, "horas,", minutos, "minutos y", segundos, "segundos")