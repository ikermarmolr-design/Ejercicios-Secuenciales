
monedas2e = int(input("Cuántas monedas de 2 euros tienes: "))
monedas1e = int(input("Cuántas monedas de 1 euro tienes: "))
monedas50 = int(input("Cuántas monedas de 50 céntimos tienes: "))
monedas20 = int(input("Cuántas monedas de 20 céntimos tienes: "))
monedas10 = int(input("Cuántas monedas de 10 céntimos tienes: "))

total_centimos = monedas2e * 200 + monedas1e * 100 + monedas50 * 50 + monedas20 * 20 + monedas10 * 10

euros = total_centimos // 100
centimos = total_centimos % 100

print("Tienes", euros, "euros y", centimos, "céntimos")