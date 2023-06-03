N = int(input("Введите количество элементов в массиве: "))

A = []
for _ in range(N):
    el = int(input("Введите элемент массива: "))
    A.append(el)

X = int(input("Введите число X: "))

new_el = None
min_dif = float('inf')

for el in A:
    dif = abs(el - X)
    if dif < min_dif:
        min_dif = dif
        new_el = el

print(f"Самый близкий к числу {X} элемент в массиве: {new_el}")
