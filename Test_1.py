# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

st = (input('Введите число: '))
ch = int(st)
print(st + ' это строка')
print(" А %s , уже число" % ch)

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec = int(input('Введите время в секундах, а я постараюсь перевести его в часы. минуты и секунды :'))
chas = sec // 3600
min = sec // 60
sec_sec = sec % 60
format = ' Время %s : %s : %s'

print(format % (chas, min, sec_sec))

# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число
# Считаем 3 + 33 + 333 = 369.

n = input(' Введите число :')
n1 = int(n)
n2 = int(n * 2)
n3 = int(n * 3)
s = n1 + n2 + n3

format = '%s + %s + %s = %s'

print(format % (n1, n2, n3, s))

# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

a = input('Введите целое положительное число :')
max = 0
i = 0

while i < len(a):
    if int(a[i]) > max:
        max = int(a[i])
    i = i + 1

print('Самая большая цифра в введеном вами числе: ' + str(max))

# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


deb = int(input('Введите сумму вашей выручки : '))
crd = int(input('Введите сумму ваших издержек : '))
if deb > crd:
    print('Ваша прибыль составила ' + str(deb - crd) + ' рублей')
    print('Рентабельность вашей деятельности  составила ' + str((deb // (deb - crd)) * 100) + ' %')
    p = int(input('Введите количество сотрудников вашего предприятия :'))
    print('Прибыль фирмы в расчете на одного сотрудника составляет ' + str((deb - crd) // p) + ' рублей')
if deb < crd:
    print('Ваша убыток составил ' + str(deb - crd) + ' рублей')
if deb == crd:
    print('Ваша доход равен вашим расходам ' + ' рублей')

# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input('Введите результат пробежки в первый день (км) : '))

b = int(input('Введите целевое значение (км) : '))
i = 1  # счетчик дней
d = a  # результат в очередной (i) день
while d < b:
    prirost = (d / 100) * 10  # ежедневный прирост результата
    d = d + prirost
    i = i + 1
print('Целевое значение будет достигнуто на ' + str(i) + ' день')
