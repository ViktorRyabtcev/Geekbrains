"""
Задание 3.

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
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
my_dict = {"ООО УСЦ  АФИА ": 789456, "ООО  УЦ ГОРОД ЗНАНИЙ ": 900456, "ООО  ФАЯЛИТ ": 678345,
           "ООО  ТХС  ДЕРЕВО ": 34567, "ООО  ЦЕНТР ПЕСОЧНОГО ТВОРЧЕСТВА ": 32456, "ООО  ВК ": 878456,
           "ООО  КАШТАН ": 456789, "ООО  АКАДЕМИЯ ПРАКТИЧЕСКОГО МЕНЕДЖМЕНТА ": 978652, "ООО  РАКЕТА ": 345096,
           "ООО  СМАЙЛ ": 264864, "ООО  АРБАТ ": 763706, "ООО  ЮНИУМ-ДВ ": 964245, "ООО  ЦКП ВЕКТОР ": 4567857,
           "ООО  ТЕМА ПЛЮС ": 65374764, "ООО  СТУДИЯ ТВОРЧЕСТВА ДО-ДО ": 63563456,
           "МБУДО  ДШИ № 3 Г. ВЛАДИВОСТОКА ": 3467346, "МАУ ДО  ЦЕНТРИНФОРМ ": 42572476,
           "МБУДО  ДШИ № 5 Г. ВЛАДИВОСТОКА ": 4672467, "МБУДО  ДМШ № 2 Г. ВЛАДИВОСТОКА ": 246723476,
           "МБУДО  ДШИ № 8 ИМ. А.В. ВОРОБЬЕВА Г. ВЛАДИВОСТОКА ": 536783356, "МБУДО  ДШИ № 1 Г. ВЛАДИВОСТОКА ": 466737,
           "МБУДО  ДШИ № 4 Г. ВЛАДИВОСТОКА ": 673423467}

''' Думаю O(1), т.к. применена встроенная функция и для вывода взят срез, 
так же выполняемый "под капотом". И это решение будет самым оптимальным т.к. все делается встроенными функциями.
'''
sort_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
print('Первые три максимальные значения :')
print(sort_dict[:3])

''' Думаю, здесь сложность линейная, O(N)
т.к. используется цикл и количество операций в нем это количество требуемых элементов.'''
sort_dict = sorted(my_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
print()
print('Первые три максимальные значения :')

counter = 1
while counter < 4:
    print(sort_dict[counter])
    counter = counter + 1

''' Можно еще и сортировку произвести в цикле, 
но сложность это явно увеличит по сравнению с остальными вариантами '''


