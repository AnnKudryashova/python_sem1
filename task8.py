#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

xA = float(input('введите значение xA: '))
yA = float(input('введите значение yA: '))
xB = float(input('введите значение xB: '))
yB = float(input('введите значение yB: '))
S = (((xA-xB)**2+(yA-yB)**2))**0.5
print('Расстояние между двумя точками =', round(S,2))