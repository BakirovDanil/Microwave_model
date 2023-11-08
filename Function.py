import time
from tkinter import *


def Message(x):
    for i in range(x):
        print("Микроволновка работает")
        time.sleep(1)


def HolstTemperature(r_var, canvas):
    if r_var.get() == 0:
        canvas.config(bg="green")
    if r_var.get() == 1:
        canvas.config(bg="orange")
    if r_var.get() == 2:
        canvas.config(bg="red")
