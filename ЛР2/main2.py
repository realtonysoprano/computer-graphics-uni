'''
Манташев А.У. М8О-305Б-20
Лабораторная работа №2.
Задание: Разработать формат представления многогранника и процедуру его каркасной
отрисовки в ортографической и изометрической проекциях.
Обеспечить удаление невидимых линий и возможность пространственных поворотов
и масштабирования многогранника. Обеспечить автоматическое центрирование
и изменение размеров изображения при изменении размеров окна.
Вариант №14:
Прямая призма с основанием - правильный 7-угольник
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import Button


def TransparentON(event):
    axis.add_collection3d(Poly3DCollection(
        frame, facecolors=[0.5, 0.4, 0.3], alpha=0.7, linewidths=1, edgecolors='black'))


def TransparentOFF(event):
    axis.add_collection3d(Poly3DCollection(
        frame, facecolors=[0.5, 0.4, 0.3], alpha=1, linewidths=1, edgecolors='black'))


fig = plt.figure('Манташев А.У. Вариант №14. Лабораторная работа №2', figsize=(7, 6))
axis = fig.add_subplot(111, projection='3d')

buttonON = fig.add_subplot(863)
btnON = Button(buttonON, 'ON')
btnON.on_clicked(TransparentON)
btnON.color = '#778899'

buttonOFF = fig.add_subplot(864)
btnOFF = Button(buttonOFF, 'OFF')
btnOFF.on_clicked(TransparentOFF)
btnOFF.color = '#778899'

xC = 0
yC = 0
zC = 0
R = 10
H = 15
N = 7

p = np.array([
    [xC + R * np.cos(np.pi/N * (1 + 2 * 0)), yC + R * np.sin(np.pi/N * (1 + 2 * 0)), zC],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 1)), yC + R * np.sin(np.pi/N * (1 + 2 * 1)), zC],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 2)), yC + R * np.sin(np.pi/N * (1 + 2 * 2)), zC],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 3)), yC + R * np.sin(np.pi/N * (1 + 2 * 3)), zC],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 4)), yC + R * np.sin(np.pi/N * (1 + 2 * 4)), zC],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 5)), yC + R * np.sin(np.pi/N * (1 + 2 * 5)), zC],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 6)), yC + R * np.sin(np.pi/N * (1 + 2 * 6)), zC],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 0)), yC + R * np.sin(np.pi/N * (1 + 2 * 0)), zC + H],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 1)), yC + R * np.sin(np.pi/N * (1 + 2 * 1)), zC + H],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 2)), yC + R * np.sin(np.pi/N * (1 + 2 * 2)), zC + H],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 3)), yC + R * np.sin(np.pi/N * (1 + 2 * 3)), zC + H],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 4)), yC + R * np.sin(np.pi/N * (1 + 2 * 4)), zC + H],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 5)), yC + R * np.sin(np.pi/N * (1 + 2 * 5)), zC + H],
    [xC + R * np.cos(np.pi/N * (1 + 2 * 6)), yC + R * np.sin(np.pi/N * (1 + 2 * 6)), zC + H]
])
frame = [
    [p[0], p[1], p[2], p[3], p[4], p[5], p[6]],
    [p[7], p[8], p[9], p[10], p[11], p[12], p[13]],
    [p[0], p[1], p[8], p[7]],
    [p[1], p[2], p[9], p[8]],
    [p[2], p[3], p[10], p[9]],
    [p[3], p[4], p[11], p[10]],
    [p[4], p[5], p[12], p[11]],
    [p[5], p[6], p[13], p[12]],
    [p[6], p[0], p[7], p[13]],
]

axis.scatter3D(p[:, 0], p[:, 1], p[:, 2], color='black')

axis.add_collection3d(Poly3DCollection(
    frame, facecolors=[0.5, 0.4, 0.3], alpha=0.7, linewidths=1, edgecolors='black'))

axis.set_xlabel('X', fontsize=20, color='black')
axis.set_ylabel('Y', fontsize=20, color='black')
axis.set_zlabel('Z', fontsize=20, color='black')
axis.set_title('\"Призма - 7-угольник\"\nПрозрачность')

plt.show()