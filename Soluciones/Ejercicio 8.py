
sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce la venta 1: "))
venta2 = float(input("Introduce la venta 2: "))
venta3 = float(input("Introduce la venta 3: "))

comision = (venta1 + venta2 + venta3) * 0.10
total = sueldo_base + comision

print("La comisión es", comision)
print("El total del mes es", total)