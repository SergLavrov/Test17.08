
# Задача: Заполнить массив случайными положительными и отрицательными
#         числами, таким образом, чтобы все числа по модулю были разными.
#         Это значит, что в массиве не может быть ни только двух равных чисел,
#         но не может быть двух равных по модулю.
#         В полученном массиве найти наибольшее по модулю число.
#
# Пояснение: вводим randomно числа, если отрицательное то добавляем в список.
import random

lenList = int(input('Enter the length of the list: '))

someList = []

for i in range(lenList):
    i = random.randint(-100, 100)
    if i < 0:
        if i not in someList:
            someList.append(i)

print(someList)

newList = []
for ind in range(len(someList)):
    newList.append(abs(someList[ind]))

result = max(newList)

print(f'Наибольшее по модулю число: {result}')

# ВЫВОД:
# Enter the length of the list: 5
# [-95, -48, -42]
# Наибольшее по модулю число: 95



# Задача. Учитывая число N, можете ли вы изготовить два числа NE и NO чтобы NE состояло
# из четных цифр, а NO из нечетных цифр.

# N = 126453        NE = 264      NO = 153

# Вариант 1:

number = 126453

num1 = number // 100000
num2 = number % 100000 // 10000
num3 = number % 10000 // 1000
num4 = number % 1000 // 100
num5 = number % 100 // 10
num6 = number % 10

NE = num2 * 100 + num3 * 10 + num4
print('NE:', NE)

NO = num1 * 100 + num5 * 10 + num6
print('NO:', NO)


# Вариант 2:

number = 126453

num = str(number)       # Перевели число в строку
print(num)
num1 = list(num)        # Перевели строку в список
print(num1)             # метод "append" в строке НЕ работает !!!!
NE = []
NO = []

for i in num1:
    if int(i) % 2 == 0:   # НЕ забыть поставить int, т.к. перебираем числа !!!
        NE.append(i)      # и сравниваем их с числом 0.
    else:
        NO.append(i)

# Можно этот блок сделать так:
# for i in range(len(num1)):
#     if int(num1[i]) % 2 == 0:    # НЕ забыть поставить int, т.к. перебираем числа !!!
#         NE.append(num1[i])       # и сравниваем их с числом 0.
#     else:
#         NO.append(num1[i])

result1 = int(''.join(NE))    # Перевели список в строку при помощи ''.join,
result2 = int(''.join(NO))    # а затем сразу перевели строку в натур число - int()

print(result1)
print(result2)

# ВЫВОД:
# 126453
# ['1', '2', '6', '4', '5', '3']
# 264
# 153


# Задача.
# Если мы перечислим все натуральные числа до 10, кратные 3 или 5, то получим
# 3, 5, 6 и 9. Сумма этих кратных равна 23.
# Завершите решение так, чтобы оно вернуло сумму всех кратных 3 или 5 ниже переданного числа.
# Кроме того, если число отрицательное верните 0 (для языков, в которых они есть).
# Примечание: если число кратно 3 и 5, посчитайте его только один раз.

number = 10
sum = 0
for i in range(1, number):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        sum += i
print(sum)

print('-----------------')

number1 = sum      # (Число 23)
sum1 = 0
for i in range(1, sum):
    if i % 3 == 0 or i % 5 == 0:
       if i % 3 == 0 and i % 5 == 0:
            continue
       print(i)
       sum1 += i

print(sum1)
