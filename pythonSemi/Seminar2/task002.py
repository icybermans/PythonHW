# определить номер числа Фибоначчи по его значению



a = 0
b = 1
k = 0

mas = [a, b]
while k != 12:
    temp = b
    b = a + b
    a = temp
    mas.append(b)
    k += 1
    #print(mas[k])

m = int(input("Ввести некое число: "))
w = 0
flag = True
while w != len(mas):
    if m == mas[w]:
        print(f"Да, это число Фибоначии. Его номер равен {w+1}")
        flag = True
        break
    else:
        flag = False
    w += 1
if flag == False:
    print(-1)
    