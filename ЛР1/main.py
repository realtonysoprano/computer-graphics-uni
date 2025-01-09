'''
Манташев А. М8О-305Б-20
Лабораторная работа №1.
Задание: Написать и отладить программу, строящую изображение заданной замечательной кривой.
Вариант №3:
x = a * cos^3(phi)
y = a * sin^3(phi)
'''

import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.axisartist import SubplotZero

import random

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.initialize()

    def initialize(self):
        self.title('y=asin^3(phi); x=acos^3(phi)')

        button = tk.Button(self, text='Quit', command=self.on_click)
        button.pack(side=tk.BOTTOM)

        self.a = tk.DoubleVar()
        self.a.set(5.0)

        slider_a = tk.Scale(self, from_=10, to=1, resolution=0.1,
                            label='a', variable=self.a,
                            command=self.on_change)
        slider_a.pack(side=tk.LEFT, padx = 0, fill=None, expand=False)


        x, y = self.data(self.a.get())
        self.fig, self.ax = self.configure_plot()

        xBorder, yBorder = self.calculate_borders(x, y)

        xlim = (-xBorder, xBorder)
        ylim = (-yBorder, yBorder)

        self.change_limits(xlim, ylim)

        self.draw_text(xBorder, yBorder)

        self.line1, = self.ax.plot(x, y, color=random.choice(['red', 'green', 'blue', 'black', 'orange']))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()

        self.canvas.draw()


    def on_click(self):
        self.quit()

    def on_change(self, value):
        x, y = self.data(self.a.get())
        xBorder, yBorder = self.calculate_borders(x, y)

        xlim = (-xBorder, xBorder)
        ylim = (-yBorder, yBorder)

        self.change_limits(xlim, ylim)
        self.line1.set_data(x, y)

        for i in range(len(self.ax.texts)):
            self.ax.texts[i].set_visible(False)

        self.draw_text(xBorder, yBorder)

        self.canvas.draw()

    @staticmethod
    def change_limits(xlim, ylim):
        plt.xlim(xlim)
        plt.ylim(ylim)

    @staticmethod
    def calculate_borders(x, y):
        xmin = -10
        xmax = 10
        ymin = 0
        ymax = 10
        xBorder = max(abs(min(min(x), xmin)), abs(max(max(x), xmax)))
        yBorder = max(abs(min(min(y), ymin)), abs(max(max(y), ymax)))

        return xBorder, yBorder

    def draw_text(self, xBorder, yBorder):
        self.ax.text(xBorder, yBorder / 20, 'X', size=10, bbox=dict(facecolor='orange', alpha=0.3))
        self.ax.text(xBorder / 20, yBorder, 'Y', size=10, bbox=dict(facecolor='orange', alpha=0.3))

    @staticmethod
    def configure_plot():
        fig = plt.figure(1)
        plt.style.use('seaborn-bright')
        ax = SubplotZero(fig, 111)
        fig.add_subplot(ax)

        for direction in ['xzero', 'yzero']:
            ax.axis[direction].set_axisline_style('-|>')
            ax.axis[direction].set_visible(True)

        for direction in ['left', 'right', 'bottom', 'top']:
            ax.axis[direction].set_visible(False)

        plt.grid()
        plt.title('$y=asin^3(phi); x=acos^3(phi)$')

        return fig, ax

    @staticmethod
    def data(a):
        Phi = np.linspace(0, 10, 100)

        x = a * np.power(np.cos(Phi), 3)
        y = a * np.power(np.sin(Phi), 3)

        return x, y


if __name__ == '__main__':
    app = App()
    app.mainloop()