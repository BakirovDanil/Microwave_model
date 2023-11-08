from datetime import datetime
from tkinter import *
from tkinter import ttk
import Function
import Microwave

Frame = Tk()
# отслеживание режима работы
r_var_mode = IntVar()
r_var_mode.set(0)
# отслеживание выбранной температуры
r_var_temperature = IntVar()
r_var_temperature.set(0)
# отслеживание выбранного времени
time = IntVar()
time.set(0)

# поле для вывода текущего времени
times = ttk.Label()
times.place(x=900, y=460)
times['foreground'] = 'green'
times['font'] = ('TimesNewRoman', 14)
times['background'] = 'black'

# создание выборов режима температуры
radiotemp1 = ttk.Radiobutton(variable=r_var_temperature, text="40 градусов", value=0)
Microwave.Sozdanie1(radiotemp1, 680, 70)
radiotemp2 = ttk.Radiobutton(variable=r_var_temperature, text="70 градусов", value=1)
Microwave.Sozdanie1(radiotemp2, 680, 110)
radiotemp3 = ttk.Radiobutton(variable=r_var_temperature, text="100 градусов", value=2)
Microwave.Sozdanie1(radiotemp3, 680, 150)
tempa = [radiotemp1, radiotemp2, radiotemp3]
# создание выбора времени работы
radiotime1 = ttk.Radiobutton(variable=time, text="1 минута", value=0)
Microwave.Sozdanie1(radiotime1, 820, 270)
radiotime2 = ttk.Radiobutton(variable=time, text="1 м. 30 секунд", value=1)
Microwave.Sozdanie1(radiotime2, 820, 310)
radiotime3 = ttk.Radiobutton(variable=time, text="2 минуты", value=2)
Microwave.Sozdanie1(radiotime3, 820, 350)
radiotime4 = ttk.Radiobutton(variable=time, text="2 м. 30 секунд", value=3)
Microwave.Sozdanie1(radiotime4, 820, 390)
radiotime5 = ttk.Radiobutton(variable=time, text="3 минуты", value=4)
Microwave.Sozdanie1(radiotime5, 820, 430)
timer = [radiotime1, radiotime2, radiotime3, radiotime4, radiotime5]
# создание выборов режима работы
radiomode1 = ttk.Radiobutton(variable=r_var_mode, text="Пользовательский режим", value=0, command=Function.on_radio_select(r_var_mode,timer,tempa))
Microwave.Sozdanie1(radiomode1, 820, 70)
radiomode2 = ttk.Radiobutton(variable=r_var_mode, text="Режим подогрева", value=1, command=Function.on_radio_select(r_var_mode,timer,tempa))
Microwave.Sozdanie1(radiomode2, 820, 110)
radiomode3 = ttk.Radiobutton(variable=r_var_mode, text="Режим разморозки", value=2, command=Function.on_radio_select(r_var_mode,timer,tempa))
Microwave.Sozdanie1(radiomode3, 820, 150)
radiomode4 = ttk.Radiobutton(variable=r_var_mode, text="Режим готовки", value=3, command=Function.on_radio_select(r_var_mode,timer,tempa))
Microwave.Sozdanie1(radiomode4, 820, 190)




def update_time():
    times.config(text=f"{datetime.now():%H:%M:%S}")
    Frame.after(100, update_time)


def Finish():
    Frame.destroy()
    print("Закрытие приложений")




def MainForm(window):
    window.title("Бакиров Данил, Валеев Марат. Моделирование работы микроволновки")
    window.geometry("1000x500+400+200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", Finish)
    # Создание полей подсказок Label
    label = Microwave.Label()
    label.Sozdanie(Frame)
    # Метод, который запускает основную форму
    window.mainloop()


update_time()
MainForm(Frame)
