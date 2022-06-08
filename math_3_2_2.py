# vector*********
print("введите координаты вектора a(x,y,z)")

# Импортируем библиотеку для работы с математикой
import math

# Запрашиваем координаты X, Y, Z
x = float(input('X = '))
y = float(input('Y = '))
z = float(input('Z = '))

# Вычисляем длину вектора
lvec = math.sqrt(x * x + y * y + z * z)

# Выводим длину вектора
print('a = ', lvec)
