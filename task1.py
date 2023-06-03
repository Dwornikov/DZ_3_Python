N = int(input("Введите количество элементов в массиве: "))

A = []
for _ in range(N):
    element = int(input("Введите элемент массива: "))
    A.append(element)

X = int(input("Введите число X: "))

count = 0
for element in A:
    if element == X:
        count += 1

print(f"Число {X} встречается {count} раз(а) в массиве.")
