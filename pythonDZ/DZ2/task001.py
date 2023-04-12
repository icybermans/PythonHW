# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые 
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же 
# стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random

N = int(input("Укажите количество монеток на столе: "))
coins = []
for i in range(N):
    oneCoin = random.randint(0, 1)
    coins.append(oneCoin)
    print(oneCoin, end = ' ')

countZeros = 0
countOnes = 0
for i in coins:
    if i == 0:
        countZeros += 1
    elif i == 1:
        countOnes += 1

# по сути, минимальное количество действий равно наименьшему из этих 2х количеств
if countZeros >= countOnes:
    print('\n', f" ===> нужно перевернуть {countOnes} монеток")
else:
    print('\n', f" ===> нужно перевернуть {countZeros} монеток")