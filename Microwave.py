from tkinter import *
from tkinter import ttk
from abc import ABC


def ParametrsLabel(labels):
    for i in labels:
        i['foreground'] = 'blue'
        i['font'] = ('time1sNewRoman', 11)


class Figure(ABC):

    def Sozdanie(self, window):
        pass


class Label(Figure):
    def Sozdanie(self, window):
        Mode = ttk.Label(text="Режим работы")
        Mode.place(x=820, y=30)
        Temperature = ttk.Label(text="Температура")
        Temperature.place(x=680, y=30)
        time1 = ttk.Label(text="Время подогрева")
        time1.place(x=820, y=230)
        data = ttk.Label(text="Текущее время")
        data.place(x=790, y=462)
        labels = [Mode, Temperature, time1, data]
        ParametrsLabel(labels)


def Sozdanie1(label, x, y):
    label.place(x=x, y=y)