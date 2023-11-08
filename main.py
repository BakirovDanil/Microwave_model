import threading
from datetime import datetime
from tkinter import *
from tkinter import ttk
import time
import tkinter as tk

import Function
import Microwave

Frame = Tk()
python_image = PhotoImage(file="Food.png")
python_image = python_image.subsample(3, 3)
# отслеживание режима работы
r_var_mode = IntVar()
r_var_mode.set(0)
# отслеживание выбранной температуры
r_var_temperature = IntVar()
r_var_temperature.set(0)
# отслеживание выбранного времени
time1 = IntVar()
time1.set(0)

# поле для вывода текущего времени
time1s = ttk.Label()
time1s.place(x=900, y=460)
time1s['foreground'] = 'green'
time1s['font'] = ('time1sNewRoman', 14)
time1s['background'] = 'black'

canvas = Canvas(bg="#5599FF", width=640, height=480)
canvas.place(x=10, y=10)


# Работа RadioButton в зависимости от выбранного флага
def on_radio_select():
    if r_var_mode.get() == 0:
        for i in tempa:
            i.config(state="normal")
        for i in time1r:
            i.config(state="normal")
    elif r_var_mode.get() == 1:
        r_var_temperature.set(1)
        time1.set(2)
        for i in tempa:
            i.config(state="disabled")
        for i in time1r:
            i.config(state="disabled")
    elif r_var_mode.get() == 2:
        r_var_temperature.set(0)
        time1.set(4)
        for i in tempa:
            i.config(state="disabled")
        for i in time1r:
            i.config(state="disabled")
    elif r_var_mode.get() == 3:
        r_var_temperature.set(2)
        time1.set(3)
        for i in tempa:
            i.config(state="disabled")
        for i in time1r:
            i.config(state="disabled")


def Vibor():
    if r_var_mode.get() == 0:
        if r_var_temperature.get() == 0:
            if time1.get() == 0:
                print("Пользовательский режим с температурой 40 градусов и временем  1 минута")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(6))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 1:
                print("Пользовательский режим с температурой 40 градусов и временем  1 минута 30 секунд")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(9))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 2:
                print("Пользовательский режим с температурой 40 градусов и временем  2 минуты")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(12))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 3:
                print("Пользовательский режим с температурой 40 градусов и временем  2 минуты 30 секунд")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(15))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 4:
                print("Пользовательский режим с температурой 40 градусов и временем  3 минуты")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(18))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
        elif r_var_temperature.get() == 1:
            if time1.get() == 0:
                print("Пользовательский режим с температурой 70 градусов и временем  1 минута")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(6))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 1:
                print("Пользовательский режим с температурой 70 градусов и временем  1 минута 30 секунд")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(9))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 2:
                print("Пользовательский режим с температурой 70 градусов и временем  2 минуты")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(12))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 3:
                print("Пользовательский режим с температурой 70 градусов и временем  2 минуты 30 секунд")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(15))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 4:
                print("Пользовательский режим с температурой 70 градусов и временем  3 минуты")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(18))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
        elif r_var_temperature.get() == 2:
            if time1.get() == 0:
                print("Пользовательский режим с температурой 100 градусов и временем  1 минута")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(6))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 1:
                print("Пользовательский режим с температурой 100 градусов и временем  1 минута 30 секунд")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(9))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 2:
                print("Пользовательский режим с температурой 100 градусов и временем  2 минуты")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(12))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 3:
                print("Пользовательский режим с температурой 100 градусов и временем  2 минуты 30 секунд")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(15))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
            elif time1.get() == 4:
                print("Пользовательский режим с температурой 100 градусов и временем  3 минуты")
                microwave_thread = threading.Thread(
                    target=lambda: start_microwave(18))  # Используйте lambda для передачи аргументов
                microwave_thread.start()
    elif r_var_mode.get() == 1:
        print("Режим подогрева")
        microwave_thread = threading.Thread(
            target=lambda: start_microwave(12))  # Используйте lambda для передачи аргументов
        microwave_thread.start()
    elif r_var_mode.get() == 2:
        print("Режим разморозки")
        microwave_thread = threading.Thread(
            target=lambda: start_microwave(18))  # Используйте lambda для передачи аргументов
        microwave_thread.start()
    elif r_var_mode.get() == 3:
        print("Режим готовки")
        microwave_thread = threading.Thread(
            target=lambda: start_microwave(15))  # Используйте lambda для передачи аргументов
        microwave_thread.start()


def start_microwave(x):
    print("Микроволновка начала работу")
    t = threading.Thread(target=Function.Message, args=(x,))
    t.start()
    time.sleep(x)  # Пример: микроволновка работает в течение x секунд
    Function.HolstTemperature(r_var_temperature, canvas)  # Предполагается, что canvas доступен в области видимости
    python_image1 = canvas.create_image(150, 30, anchor=NW,
                                        image=python_image)  # Предполагается, что python_image доступен в области видимости
    print("Микроволновка закончила работу")
    time.sleep(2)
    canvas["bg"] = "#5599FF"
    canvas.delete(python_image1)


button = tk.Button(text="Начать работу", height=10, background="blue", foreground="white", command=Vibor)
button.place(x=680, y=190)

# создание выборов режима температуры
radiotemp1 = ttk.Radiobutton(variable=r_var_temperature, text="40 градусов", value=0)
Microwave.Sozdanie1(radiotemp1, 680, 70)
radiotemp2 = ttk.Radiobutton(variable=r_var_temperature, text="70 градусов", value=1)
Microwave.Sozdanie1(radiotemp2, 680, 110)
radiotemp3 = ttk.Radiobutton(variable=r_var_temperature, text="100 градусов", value=2)
Microwave.Sozdanie1(radiotemp3, 680, 150)
tempa = [radiotemp1, radiotemp2, radiotemp3]
# создание выбора времени работы
radiotime11 = ttk.Radiobutton(variable=time1, text="1 минута", value=0)
Microwave.Sozdanie1(radiotime11, 820, 270)
radiotime12 = ttk.Radiobutton(variable=time1, text="1 м. 30 секунд", value=1)
Microwave.Sozdanie1(radiotime12, 820, 310)
radiotime13 = ttk.Radiobutton(variable=time1, text="2 минуты", value=2)
Microwave.Sozdanie1(radiotime13, 820, 350)
radiotime14 = ttk.Radiobutton(variable=time1, text="2 м. 30 секунд", value=3)
Microwave.Sozdanie1(radiotime14, 820, 390)
radiotime15 = ttk.Radiobutton(variable=time1, text="3 минуты", value=4)
Microwave.Sozdanie1(radiotime15, 820, 430)
time1r = [radiotime11, radiotime12, radiotime13, radiotime14, radiotime15]
# создание выборов режима работы
radiomode1 = ttk.Radiobutton(variable=r_var_mode, text="Пользовательский режим", value=0,
                             command=on_radio_select)
Microwave.Sozdanie1(radiomode1, 820, 70)
radiomode2 = ttk.Radiobutton(variable=r_var_mode, text="Режим подогрева", value=1,
                             command=on_radio_select)
Microwave.Sozdanie1(radiomode2, 820, 110)
radiomode3 = ttk.Radiobutton(variable=r_var_mode, text="Режим разморозки", value=2,
                             command=on_radio_select)
Microwave.Sozdanie1(radiomode3, 820, 150)
radiomode4 = ttk.Radiobutton(variable=r_var_mode, text="Режим готовки", value=3,
                             command=on_radio_select)
Microwave.Sozdanie1(radiomode4, 820, 190)


def update_time1():
    time1s.config(text=f"{datetime.now():%H:%M:%S}")
    Frame.after(100, update_time1)


def Finish():
    Frame.destroy()
    print("Закрытие приложения")


def MainForm(window):
    window.title("Бакиров Данил, Валеев Марат, Баембитов Гата, Газизов Линар. Моделирование работы микроволновки")
    window.geometry("1000x500+400+200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", Finish)
    # Создание полей подсказок Label
    label = Microwave.Label()
    label.Sozdanie(Frame)
    # отрисовка на Canvas
    # Метод, который запускает основную форму
    window.mainloop()


update_time1()
MainForm(Frame)
