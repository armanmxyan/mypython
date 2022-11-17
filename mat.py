#!/bin/python3

import matplotlib.pyplot as plt
#plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
#plt.show()
from math import sin 
import numpy as np
# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 20, 5000)
#y1 = x/10
#y2=x**2/100
#y3 = np.sin(x)
y3=0
for i in range(1,1000,2):
    y3=y3+np.sin(i*x)/i

# Построение графика
plt.figure(figsize=(15, 9))
plt.title("Линейная зависимость y = x") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x,y3)  # построение графика
plt.show()

'''
# Линейная зависимость
x = np.linspace(0, 10, 50)
y1 = x
# Квадратичная зависимость
y2 = [i**2 for i in x]
# Построение графиков
plt.figure(figsize=(9, 9))
plt.subplot(2, 1, 1)
plt.plot(x, y1)               # построение графика
plt.title("Зависимости: y1 = x, y2 = x^2") # заголовок
plt.ylabel("y1", fontsize=14) # ось ординат
plt.grid(True)                # включение отображение сетки
plt.subplot(2, 1, 2)
plt.plot(x, y2)               # построение графика
plt.xlabel("x", fontsize=14)  # ось абсцисс
plt.ylabel("y2", fontsize=14) # ось ординат
plt.grid(True)                # включение отображение сетки
plt.show()
'''
