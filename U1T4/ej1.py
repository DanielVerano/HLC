# Invierta la siguiente tupla

tupla = (10, 20, 30, 40, 50)
tupla_inv = ()

for n in reversed(tupla):
    tupla_inv = tupla_inv + (n,)
print(tupla_inv)