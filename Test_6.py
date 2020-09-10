# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# в рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    _color = None
    _colors = ['Красный', 'Желтый', 'Зеленый']
    _time = [7, 2, 3]

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i = 0
        while i < 3: # Количество циклов работы светофора
            for i in range(0,3):
                print(TrafficLight._colors[i])
                sleep_time = TrafficLight._time[i]
                print('Пауза продолжительностью {} секунд.'.format(sleep_time))
                time.sleep(sleep_time)
                i +=1


print('Модель работы светофора')
traffic = TrafficLight()
traffic.running()

# 2 Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода. Например: 20м*5000м*25кг*5см = 12500 т


class Road():
    __length = None
    __width = None
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc (self):
        self.weigth = 25
        self.tickness = 0.005
        calculate = self.__length * self.__width * self.weigth * self.tickness
        print('Необходимая масса асфальта составит {} т'.format(calculate))


road_to_Vladivostok = Road (5000, 20)
road_to_Vladivostok.calc()

# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker():
    name = None
    surname = None
    position = None
    wage = None
    bonus = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        self.__income = {'wage': self.wage, 'bonus': self.bonus}
        return self.__income

manager = Position('Ivan', 'Petrov', 'manager', 500, 100)
print(manager.get_full_name())
print(manager.get_total_income())

# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    speed = None
    color = None
    name = None
    is_polis = None

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polis = is_police

    def show_speed(self):
        speed = self.speed
        print('Cкорость ' + self.color+ ' ' + self.name + ' {} км/ч '.format(speed))

    def go(self):
        print(self.color+ ' ' + self.name + ' едет прямо')

    def stop(self):
        print(self.color+ '  ' + self.name +' остановилась')

    def turn(self, direction):
        self.direction = direction
        print(self.color+ ' ' + self.name +' повернула в направлении ' + direction)


class TownCar(Car):
    family = None
    def __init__(self, speed, color, name, is_polis):
        super().__init__( speed, color, name, is_polis)
        self.family = family

    def show_speed(self):
        if self.speed > 40:
            print(self.color+ '  ' + self.name + ', Ваша скорость {} км/ч '.format(self.speed))
            print('Вы превысили скорость на {} км/ч'.format(self.speed - 40))
        else:
            print('Cкорость ' + self.color + ' ' + self.name + ' {} км/ч '.format(self.speed))

class SportCar(Car):
    def __init__(self, speed, color, name, is_polis):
        super().__init__(speed, color, name, is_polis)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_polis):
        super().__init__(speed, color, name, is_polis)

    def show_speed(self):
        if self.speed > 40:
            print(self.color+ '  ' + self.name + ', Ваша скорость {} км/ч '.format(self.speed))
            print('Вы превысили скорость на {} км/ч'.format(self.speed - 40))
        else:
            print('Cкорость ' + self.color + ' ' + self.name + ' {} км/ч '.format(self.speed))



class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

ford = WorkCar(50, 'red', 'Ford', False)
sport = SportCar(90, 'red', 'Ford', False)
work1 = WorkCar(30, 'green', 'Ford', False)
work2 = WorkCar(60, 'green', 'Ford', False)
police = PoliceCar(100, 'black', 'Ford')
ford.go()
sport.turn('Left')
police.show_speed()
police.stop()
work2.show_speed()
work1.show_speed()


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery ():

    title = None

    def __init__(self, title):
        self.title = title

    def draw (self):
        print('Запуск отрисовки.')


class Pen (Stationery):
    def draw(self):
        print('Запуск отрисовки, с использованием {} .'.format(self.title))

class Pencil (Stationery):
    def draw(self):
        print('Запуск отрисовки, с использованием {} .'.format(self.title))

class Handle (Stationery):
    def draw(self):
        print('Запуск отрисовки, с использованием {} .'.format(self.title))

my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')
my_Stationery = Stationery ('Не известная фигня')
my_Stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()