# Modifique el primer elemento (22) de una lista dentro de una tupla siguiente a 222

tupla = (11, [22, 33], 44, 55)

# for n in tupla:
#     if type(n) == list:
#         n[0] = 222

tupla[1][0] = 222

print(tupla)