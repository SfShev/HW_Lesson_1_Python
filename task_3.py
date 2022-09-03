# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_dots(x):
    xy = ["x","y"]
    dots = []
    for i in range(x):
        dots.append(float(input(f"Введите точку {xy[i]}: ")))

    return dots 

def location_chek (x):
    quarter = 0
    if x[0] > 0 and x[1] > 0 :
        quarter = 1
    elif x[0] < 0 and x[1] < 0 :
        quarter = 3 
    elif x[0] < 0 and x[1] > 0 :
        quarter = 2
    elif x[0] > 0 and x[1] < 0 :
        quarter = 4
    print (f"Точка в {quarter} четверти")

a = input_dots(2)
location_chek(a)
