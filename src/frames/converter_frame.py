import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from constants.frames import MAIN_FRAME_NAME


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
        self.main_label.pack(pady=35)

        self.first_info_label = tk.Label(self, text="Изначальная единица измерения", font="Helvetica 15")
        self.first_info_label.pack(pady=5)

        self.first_unit_selector = ttk.Combobox(self, values=list(self.units.keys()), justify='center',
                                                textvariable=self.selected_unit_one)
        self.first_unit_selector['state'] = 'readonly'
        self.first_unit_selector.pack()

        self.second_info_label = tk.Label(self, text="Конвертируемое значение", font="Helvetica 15")
        self.second_info_label.pack(pady=5)

        self.first_entry = tk.Entry(self, width=24)
        self.first_entry.pack()

        self.third_info_label = tk.Label(self, text="Конечная единица измерения", font="Helvetica 15")
        self.third_info_label.pack(pady=5)

        self.second_unit_selector = ttk.Combobox(self, values=list(self.units.keys()), justify='center',
                                                 textvariable=self.selected_unit_two)
        self.second_unit_selector['state'] = 'readonly'
        self.second_unit_selector.pack()

        self.fourth_info_label = tk.Label(self, text="Результат конвертации", font="Helvetica 15")
        self.fourth_info_label.pack(pady=5)

        self.second_entry = tk.Entry(self, width=24)
        self.second_entry.pack()
        self.second_entry.configure(state='readonly')

        self.convert_button = tk.Button(self, text="Конвертировать", width=20, height=3, command=self.convert)
        self.convert_button.pack(pady=40)
        self.back_button = tk.Button(self, text="Назад", width=20, height=3,
                                     command=lambda: self.controller.show_frame(MAIN_FRAME_NAME))
        self.back_button.pack()

    def render(self):
        self.__clear()

        selected_unit = self.controller.selected_quantity.get()
        self.main_label["text"] = "Выбрана величина: {}".format(selected_unit)

        for unit in self.controller.phys_quantities[selected_unit]:
            self.units[unit.name] = unit

        self.first_unit_selector["values"] = list(self.units.keys())
        self.second_unit_selector["values"] = list(self.units.keys())

    def __clear(self):
        self.units = {}
        self.first_unit_selector.set("")
        self.second_unit_selector.set("")
        self.first_entry.delete(0, tk.END)
        self.second_entry.configure(state="normal")
        self.second_entry.delete(0, tk.END)
        self.second_entry.configure(state="readonly")

    def convert(self):
        gotten_value_str = self.first_entry.get()
        first_unit_str = self.selected_unit_one.get()
        second_unit_str = self.selected_unit_two.get()

        if gotten_value_str == '' or first_unit_str == '' or second_unit_str == '':
            showerror("Некорректные данные", "Заполните все поля для конвертации")
            return

        try:
            gotten_value = float(gotten_value_str)
        except ValueError:
            showerror("Введите корректные данные", "Введите числовое значение")
            return

        gotten_first_unit = self.units[first_unit_str]
        gotten_second_unit = self.units[second_unit_str]

        if gotten_first_unit.conversion_operation == "*":
            first_step_value = gotten_value * gotten_first_unit.conversion_factor
        elif gotten_first_unit.conversion_operation == "+":
            first_step_value = gotten_value + gotten_first_unit.conversion_factor

        if gotten_second_unit.conversion_operation == "*":
            second_step_value = first_step_value / gotten_second_unit.conversion_factor
        elif gotten_second_unit.conversion_operation == "+":
            second_step_value = first_step_value - gotten_second_unit.conversion_factor

        self.second_entry.configure(state="normal")
        self.second_entry.delete(0, tk.END)
        self.second_entry.insert(0, second_step_value)
        self.second_entry.configure(state="readonly")
