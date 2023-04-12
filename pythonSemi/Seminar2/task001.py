# вычислить факториал числа N, используя цикл while

n = int(input("Введите натуральное число: "))
multi = 1

while n != 0:
    multi *= n
    n -= 1

print(multi)