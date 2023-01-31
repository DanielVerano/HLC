# Agregue el elemento 7000 después de 6000 en la siguiente lista

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

sublist1 = list1[2]
sublist2 = sublist1[2]
sublist2.append(7000)

print(list1)