
distancia = float(input("Introduce la distancia entre los vehículos (km): "))
v1 = float(input("Introduce la velocidad del vehículo de atrás (km/h): "))
v2 = float(input("Introduce la velocidad del vehículo de delante (km/h): "))

tiempo_horas = distancia / (v1 - v2)
tiempo_minutos = tiempo_horas * 60

print("Lo alcanzará en", tiempo_minutos, "minutos")