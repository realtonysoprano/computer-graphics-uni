'''
Манташев А.У. М8О-305Б-20
Лабораторная работа №7.
Задание: Написать программу, строящую полиномиальную кривую
по заданным точкам. Обеспечить возможность изменения позиции
точек и, при необходимости, значений касательных векторов и натяжения.
Вариант №3:
Сплайн непрерывной кривизны из двух сегментов по трем точкам
и касательным в 1-й и 3-й точке.
'''


from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg

# initial values y
y01 = 50
y02 = 100
y03 = -50

# 3 points
x = [-1, 1, 3]
y = (y01, y02, y03)

# cubic spline
f = plt.figure('Манташев А.У. Лабораторная работа №7 Вариант №3.')
f = CubicSpline(x, y, bc_type='natural')
x_new = np.linspace(x[0], x[2], 100)
y_new = f(x_new)

x_val_01 = x[0]
x_val_02 = x[2]


# creating tangent at edge points
def create_line(x_val_num, f):
    x_new_num = np.linspace(x_val_num - 0.5, x_val_num + 0.5, 20)
    y_new_num = f(x_new_num)

    slope = np.gradient(y_new_num, x_new_num)

    ind_min = (np.abs(x_new_num - x_val_num)).argmin()

    if x_val_num == x_new_num[ind_min]:
        y_val_01, slope_Val = y_new_num[ind_min], slope[ind_min]
    else:
        if x_val_num < x_new_num[ind_min]:
            ind_min, ind2 = ind_min - 1, ind_min
        else:
            ind_min, ind2 = ind_min, ind_min + 1
        y_val_01 = y_new_num[ind_min] + (y_new_num[ind2] - y_new_num[ind_min]) * (x_val_num - x_new_num[ind_min]) / (
                    x_new_num[ind2] - x_new_num[ind_min])
        slope_Val = slope[ind_min] + (slope[ind2] - slope[ind_min]) * (x_val_num - x_new_num[ind_min]) / (
                    x_new_num[ind2] - x_new_num[ind_min])
    intercVal = y_val_01 - slope_Val * x_val_num

    plt.plot([x_new_num.min(), x_new_num.max()],
             [slope_Val * x_new_num.min() + intercVal, slope_Val * x_new_num.max() + intercVal], linestyle='-.',
             linewidth=1, color='orange')

def draw(f):
    f = CubicSpline(x, y, bc_type='natural')
    x_new = np.linspace(x[0], x[2], 100)
    y_new = f(x_new)
    create_line(x_val_01, f)
    create_line(x_val_02, f)
    plt.plot(x_new, y_new, 'g')
    plt.plot(x, y, '-o', color='red')
    plt.title('Сплайн непрерывной кривизны из двух сегментов.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


layout = [
    [sg.Text('Y1 = '), sg.Slider(orientation='horizontal', key='slider1', range=(-100, 100))],
    [sg.Text('Y2 = '), sg.Slider(orientation='horizontal', key='slider2', range=(-100, 100))],
    [sg.Text('Y3 = '), sg.Slider(orientation='horizontal', key='slider3', range=(-100, 100))],
    [sg.Button('Enter'), sg.Button('Exit')]]

window = sg.Window('Координаты точек', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Enter':
        y1 = int(values['slider1'])
        y2 = int(values['slider2'])
        y3 = int(values['slider3'])
        y = (y1, y2, y3)
        draw(f)
        y = (y01, y02, y03)

window.close()