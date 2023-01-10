# Escriba un programa para usar el método string.format() para formatear las siguientes tres variables según la salida esperada.

totalMoney = 1000
quantity = 3
price = 450

# resultado = f"Tengo {totalMoney} euros para comprar {quantity} tarjetas gráficas por {price:.2f} dólares."
resultado = "Tengo {1} euros para comprar {0} tarjetas gráficas por {2:.2f} dólares."

print(resultado.format(quantity, totalMoney, price))