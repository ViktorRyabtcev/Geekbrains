"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

# Думаю, что сложность здесь линейная т.к. количество арументов всегда два O(1)

login_password = {'viktor@mail.ru': '123456789'}

login = input('Введите логин: ')
password = input('Введите пароль: ')


def chec_log_pass(login, password):
    ''' Функция принимает логин и пароль,
    сверяет со значениим хранящимися в словаре,
    выдает либо приветствие в случае успеха
    либо ПАРОЛЬ НЕ ВЕРЕН. ЗАРЕГЕСТРИРУЙТЕСЬ '''
    if login in login_password:
        if password == login_password[login]:
            print('Привет, ' + login + '!!!')
        else:
            print('Пароль неверен!')
    else:
        print('Неверный логин.Зарегестрируйтесь.')


chec_log_pass(login, password)

# Думаю, что сложность здесь логарифмическая т.к. есть бинарный поиск. ( чисто по ощущениям, этот метод быстрее)

def chec_log_pass_2():
    ''' Функция не принимает параметров,
    просит ввести пару логин - пароль
    сверяет со значениим хранящимися в словаре,
    выдает либо приветствие в случае успеха
    либо ПАРОЛЬ НЕ ВЕРЕН. ЗАРЕГЕСТРИРУЙТЕСЬ '''

    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    try:
        if password == login_password[login]:
            print('Привет, ' + login + '!!!')
        else:
            print('Пароль неверен!')
    except KeyError:
        print('Неверный логин. Зарегестрируйтесь.')


chec_log_pass_2()