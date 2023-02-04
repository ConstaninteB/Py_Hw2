# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint
length = int(input("Введите количество монет: "))
random_list = []
eagls_coin = tails_coin = 0
for i in range(length):
    random_list.append(randint(0, 1))
    if i == 0:
        tails_coin += 1
    if i == 1:
        eagls_coin += 1
if eagls_coin < tails_coin:
    print(eagls_coin)
else: print(tails_coin)                    
 