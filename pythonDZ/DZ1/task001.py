a = int(input("Введите трехзначное число: "))

sum = 0
while a > 0:
    sum += a%10
    a = a//10

print(sum)