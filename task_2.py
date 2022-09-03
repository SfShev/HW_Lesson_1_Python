# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))
first = not (x or  y or  z) 
second = (not x) and (not y) and (not z)
result = first == second
if result == True:
    print ("Утверждение истино")
else:
    print ("Утверждение не истино")        