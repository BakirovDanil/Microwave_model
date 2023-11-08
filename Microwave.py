import time
from tkinter import *
from tkinter import ttk
from abc import ABC


def ParametrsLabel(labels):
    for i in labels:
        i['foreground'] = 'blue'
        i['font'] = ('TimesNewRoman', 11)


class Figure(ABC):

    def Sozdanie(self, window):
        pass


class Label(Figure):
    def Sozdanie(self, window):
        Mode = ttk.Label(text="Режим работы")
        Mode.place(x=820, y=30)
        Temperature = ttk.Label(text="Температура")
        Temperature.place(x=680, y=30)
        Time = ttk.Label(text="Время подогрева")
        Time.place(x=820, y=230)
        data = ttk.Label(text="Текущее время")
        data.place(x=790, y=462)
        labels = [Mode, Temperature, Time, data]
        ParametrsLabel(labels)


def Sozdanie1(label, x, y):
    label.place(x=x, y=y)