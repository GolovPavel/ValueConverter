import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning, showinfo

from constants.frames import *
import util


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

        self.add_new_quantity_button = tk.Button(self, text="Добавить величину", width=20, height=3,
                                                 command=self.__select_add_new_quantity)
        self.add_new_quantity_button.pack()

        self.add_new_unit_button = tk.Button(self, text="Добавить единицу", width=20, height=3,
                                             command=self.__select_add_new_unit)
        self.add_new_unit_button.pack()

        self.clear_quantities_button = tk.Button(self, text="Сброс величин", width=20, height=3,
                                                 command=self.__clear_quantities)
        self.clear_quantities_button.pack()

    def __select_quantity(self):
        if self.controller.selected_quantity.get() == "":
            showwarning("Выберите величину", "Выберите физическую величину")
            return

        self.controller.show_frame(CONVERTER_FRAME_NAME)

    def __select_add_new_quantity(self):
        self.controller.show_frame(ADD_QUANTITY_FRAME_NAME)

    def __select_add_new_unit(self):
        self.controller.show_frame(ADD_UNIT_FRAME_NAME)

    def __clear_quantities(self):
        util.set_default_quantities()
        showinfo("Величины сброшены", "Список физических величин сброшен до первоначальных")
        self.controller.show_frame(MAIN_FRAME_NAME)
        self.quantity_selector.set('')

    def render(self):
        self.quantity_selector['values'] = list(self.controller.phys_quantities.keys())
