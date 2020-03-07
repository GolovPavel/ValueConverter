import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning

from frames.frames import CONVERTER_FRAME_NAME


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

        self.controller.show_frame(CONVERTER_FRAME_NAME)

    def render(self):
        pass
