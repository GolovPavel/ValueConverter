import json
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from model.quantity import *


class Application(tk.Tk):
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.__init_base_params()
        self.__load_data()

        self.selected_quantity = tk.StringVar()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ConverterFrame, MainFrame):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainFrame.__name__)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.render()
        frame.tkraise()

    def __init_base_params(self):
        self.title("Конвертер величин")
        position_right = int(self.winfo_screenwidth() / 2 - self.WINDOW_WIDTH / 2)
        position_down = int(self.winfo_screenheight() / 2 - self.WINDOW_HEIGHT / 2)
        self.geometry("{}x{}".format(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.geometry("+{}+{}".format(position_right, position_down))
        self.resizable(False, False)

    def __load_data(self):
        with open('../resources/quantities.json') as json_file:
            json_data = json.load(json_file)
            self.phys_quantities = {}

            for quantities_json in json_data:
                physical_quantity = PhysicalQuantity.decode_from_json(quantities_json)
                self.phys_quantities[physical_quantity.name] = physical_quantity.units


class MainFrame(tk.Frame):

    def __init__(self, root, controller):
        tk.Frame.__init__(self, root)
        self.controller = controller

        self.main_label = tk.Label(self, text="Конвертер физических величин", font="Helvetica 30 bold")
        self.main_label.pack(pady=40)

        self.chose_label = tk.Label(self, text="Выберите физическую величину", font="Helvetica 20")
        self.chose_label.pack(pady=50)

        self.quantity_selector = ttk.Combobox(self, values=list(controller.phys_quantities.keys()), justify='center',
                                              textvariable=controller.selected_quantity)
        self.quantity_selector['state'] = 'readonly'
        self.quantity_selector.pack()

        self.select_quantity_button = tk.Button(self, text="Выбор", width=20, height=3, command=self.__select_quantity)
        self.select_quantity_button.pack(pady=40)

    def __select_quantity(self):
        if self.controller.selected_quantity.get() == "":
            showwarning("Выберите величину", "Выберите физическую величину")
            return

        self.controller.show_frame(ConverterFrame.__name__)

    def render(self):
        pass


class ConverterFrame(tk.Frame):

    def __init__(self, root, controller):
        tk.Frame.__init__(self, root)
        self.controller = controller

        self.units = {}
        self.selected_unit = ""
        self.selected_unit_one = tk.StringVar()
        self.selected_unit_two = tk.StringVar()

        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(4, weight=1)

        self.main_label = tk.Label(self, font="Helvetica 30 bold")
        self.main_label.grid(row=0, columnspan=3, pady=40)

        self.first_unit_selector = ttk.Combobox(self, values=list(self.units.keys()), justify='center',
                                                textvariable=self.selected_unit_one)
        self.first_unit_selector['state'] = 'readonly'
        self.first_unit_selector.grid(row=1, column=0)

        self.second_unit_selector = ttk.Combobox(self, values=list(self.units.keys()), justify='center',
                                                 textvariable=self.selected_unit_two)
        self.second_unit_selector['state'] = 'readonly'
        self.second_unit_selector.grid(row=1, column=2)

        self.first_entry = tk.Entry(self, width=24)
        self.first_entry.grid(row=2, column=0, pady=70)

        self.second_entry = tk.Entry(self, width=24)
        self.second_entry.grid(row=2, column=2, pady=70)

        self.convert_button = tk.Button(self, text="Конвертировать", width=20, height=3, command=self.convert)
        self.convert_button.grid(row=3, column=1)

        self.back_button = tk.Button(self, text="Назад", width=20, height=3,
                                     command=lambda: self.controller.show_frame(MainFrame.__name__))
        self.back_button.grid(row=4, column=1)

    def render(self):
        selected_unit = self.controller.selected_quantity.get()
        self.main_label["text"] = "Выбрана величина: {}".format(selected_unit)

        for unit in self.controller.phys_quantities[selected_unit]:
            self.units[unit.name] = unit

        self.first_unit_selector["values"] = list(self.units.keys())
        self.second_unit_selector["values"] = list(self.units.keys())

    def convert(self):
        pass
        # Здесь будет основная логика конвертации одной единицы измерения в другую.
        # Все единицы измерения для выбранной физической величины храняться в словаре self.units,
        # где ключ - название единицы измерения, а значение - объект класса Unit.
        #
        # Принцип конвертации:
        # Берем из словаря self.units выбранные пользователем физические величины и кладем их в отдельные переменные.
        # Далее берем из self.first_entry значение, которое нужно преобразовать во вторую величину.
        #
        # Далее исходную величину переводим в базовую. Тут возможно 2 исхода:
        #     1. Операция преобразования - умножение. Тогда исходную величину умножаем на conversion_factor;
        #     2. Операция преобразования - сложение. Тогда к исходной величине прибавляем conversion_factor.
        # Предположим, что получение значение это a1.
        #
        # Далее нужно преобразовать базовую величину в ту, которую выбрал пользователель во втором combobox'e.
        # Смотрим на операцию преобразования 2ой единицы измерения.
        #     1. Если это *, то a1 делим на conversion_factor;
        #     2. Если это +, то из а1 вычитаем conversion_factor.
        # Получаем переменную a2, которая уже и есть преобразованное значение.
        #
        # На последнем этапе нужно просто записать переменную a2 во self.second_entry.
        # Как это делается можешь почитать тут
        # https://stackoverflow.com/questions/16373887/how-to-set-the-text-value-content-of-an-entry-widget-using-a-button-in-tkinter