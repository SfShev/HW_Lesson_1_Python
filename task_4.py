# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

from email.policy import default
import math


quater = int(input("Введите четверть: "))
def check_range(x):
    p_inf = math.inf
    n_inf = - math.inf
    match x:
        case 1 :
            print(f"x(0:{p_inf}) ; y(0:{p_inf})")
        case 2 :
            print(f"x({n_inf}:0) ; y(0:{p_inf})")
        case 3 :
            print(f"x({n_inf}:0) ; y({n_inf}:0)")
        case 4 :
            print(f"x(0:{p_inf}) ; y({n_inf}:0)")
        case default :
            print ("Неверное значение четверти")

check_range(quater)