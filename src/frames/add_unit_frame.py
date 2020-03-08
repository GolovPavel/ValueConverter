import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

import util
from constants.frames import MAIN_FRAME_NAME
from model.unit import Unit


class AddUnitFrame(tk.Frame):

    def __init__(self, root, controller):
        tk.Frame.__init__(self, root)
        self.controller = controller

        self.main_label = tk.Label(self, text="Добавление новой единицы измерения", font="Helvetica 30 bold")
        self.main_label.pack(pady=50)

        self.name_label = tk.Label(self, text="Название величины", font="Helvetica 15")
        self.name_label.pack(pady=5)

        self.quantity_selector = ttk.Combobox(self, values=list(self.controller.phys_quantities.keys()),
                                              justify='center')
        self.quantity_selector['state'] = 'readonly'
        self.quantity_selector.pack()

        self.name_label = tk.Label(self, text="Название единицы измерения", font="Helvetica 15")
        self.name_label.pack(pady=5)

        self.unit_name_entry = tk.Entry(self, width=24)
        self.unit_name_entry.pack()

        self.factor_label = tk.Label(self, text="Фактор преобразования", font="Helvetica 15")
        self.factor_label.pack(pady=5)

        self.factor_entry = tk.Entry(self, width=24)
        self.factor_entry.pack()

        self.factor_label = tk.Label(self, text="Операция преобразования", font="Helvetica 15")
        self.factor_label.pack(pady=5)

        self.conversion_operation_selector = ttk.Combobox(self, values=["*", "+"], justify='center')
        self.conversion_operation_selector['state'] = 'readonly'
        self.conversion_operation_selector.pack()

        self.add_button = tk.Button(self, text="Добавить", width=20, height=3, command=self.__add_unit)
        self.add_button.pack(pady=40)

        self.back_button = tk.Button(self, text="Назад", width=20, height=3,
                                     command=lambda: self.controller.show_frame(MAIN_FRAME_NAME))
        self.back_button.pack()

    def __add_unit(self):
        try:
            quantity_name = self.quantity_selector.get()
            unit_name = self.unit_name_entry.get()
            conversion_factor = float(self.factor_entry.get())
            conversion_operation = self.conversion_operation_selector.get()

            new_unit = Unit(unit_name, conversion_factor, conversion_operation)
            quantities = util.get_all_quantities()

            for quantity in quantities:
                if quantity.name == quantity_name:
                    quantity.units.append(new_unit)

            util.save_quantity(quantities)
            self.controller.show_frame(MAIN_FRAME_NAME)
        except:
            showerror("Некорректные данные", "Введите корректные данные")

    def render(self):
        self.__clear()

    def __clear(self):
        self.quantity_selector.set("")
        self.unit_name_entry.delete(0, tk.END)
        self.factor_entry.delete(0, tk.END)
        self.conversion_operation_selector.set("")
