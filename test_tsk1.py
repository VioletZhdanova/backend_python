import random
import math


# Расчет дистанции между двумя точками
def distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# Функция для расчета угла между двумя точками
def get_angle(point1, point2):
    cos = round((point1[0] * point2[0] + point1[1] * point2[1]) / (
            (point1[0] ** 2 + point1[1] ** 2) ** 0.5 * (point2[0] ** 2 + point2[1] ** 2) ** 0.5), 9)
    csa = math.acos(cos)
    return csa * 180 / math.pi


def get_random_list_point():
    checklist = list()
    # Генерация точек со случайными координатами
    for i in range(n):
        checklist.append((random.randint(-100, 100), random.randint(-100, 100)))
    return checklist


def get_minimum_distance(checklist, start):
    if (0, 0) in checklist:
        return 0.0
    else:
        # Максимально возможное расстояние при рандоме точек от -100 до 100
        minimum = (100 ** 2 + 100 * 2) ** 0.5
        for i in checklist:
            if distance(i, start) < minimum:
                minimum = distance(i, start)
        return minimum


def get_maximum_distance(checklist, start):
    # Минимально возможное расстояние
    maximum = 0.0
    for i in checklist:
        if distance(i, start) > maximum:
            maximum = distance(i, start)
    return maximum


def get_mean_distance(checklist, start):
    summa = 0
    for i in checklist:
        summa += distance(i, start)
    return summa / len(checklist)


# Выборка точек для 1 периода
def get_first_period(checklist):
    period = list()
    for i in checklist:
        if i[0] >= 0 and i[1] > 0:
            period.append(i)
    return period


# Выборка точек для 2 периода
def get_second_period(checklist):
    period = list()
    for i in checklist:
        if i[0] < 0 and i[1] >= 0:
            period.append(i)
    return period


# Выборка точек для 3 периода
def get_third_period(checklist):
    period = list()
    for i in checklist:
        if i[0] <= 0 and i[1] < 0:
            period.append(i)
    return period


# Выборка точек для 4 периода
def get_fourth_period(checklist):
    period = list()
    for i in checklist:
        if i[0] > 0 and i[1] <= 0:
            period.append(i)
    return period


# Сортировка в зависимости от того, есть ли точка (0,0) в списке
def sort_by_angle(checklist):
    # Списки для каждого периода
    period1 = get_first_period(checklist)
    period2 = get_second_period(checklist)
    period3 = get_third_period(checklist)
    period4 = get_fourth_period(checklist)
    new_checklist = list()
    if (0, 0) not in checklist and period1 != list():
        period1.sort(reverse=True, key=lambda point: (point[0], point[1]))
        new_checklist.append(period1.pop(-1))
    elif (0, 0) in checklist:
        while (0, 0) in checklist:
            new_checklist.append(checklist.pop(checklist.index((0, 0))))
    period1.sort(key=lambda point: get_angle((5, 0), point))
    period2.sort(key=lambda point: get_angle((0, 5), point))
    period3.sort(key=lambda point: get_angle((-5, 0), point))
    period4.sort(key=lambda point: get_angle((0, -5), point))
    new_checklist += period2 + period3 + period4 + period1
    return new_checklist


# Ввод количества точек
n = int(input())
if n > 0:
    checklist = get_random_list_point()
    print(f"Вывод списка в первоначальном состоянии {checklist}")

    # Расчет минимального, максимального и среднего расстояний от точек до центра
    start = (0, 0)
    minimum = get_minimum_distance(checklist, start)
    maximum = get_maximum_distance(checklist, start)
    mean = get_mean_distance(checklist, start)
    print("Максимальное расстояние от центра до точки->", maximum, "\n", "Минимальное расстояние от центра до точки->",
          minimum, "\n", "Среднее расстояниеот центра до точек->",
          mean, sep='')

    checklist = sort_by_angle(checklist)
    print(f"Вывод отсортированного списка в порядке обхода против часовой срелки {checklist}")
else:
    print("Неккоректный ввод")
