import tkinter as tk
from tkinter.messagebox import showerror

from constants.frames import MAIN_FRAME_NAME
from util import add_new_quantity


class AddQuantityFrame(tk.Frame):

    def __init__(self, root, controller):
        tk.Frame.__init__(self, root)
        self.controller = controller

        self.main_label = tk.Label(self, text="Добавление новой величины", font="Helvetica 30 bold")
        self.main_label.pack(pady=50)

        self.info_label = tk.Label(self, text="Введите название величины", font="Helvetica 20")
        self.info_label.pack(pady=40)

        self.quantity_name_entry = tk.Entry(self, width=24)
        self.quantity_name_entry.pack()

        self.add_button = tk.Button(self, text="Добавить величину", width=20, height=3, command=self.__add_quantity)
        self.add_button.pack(pady=40)

        self.back_button = tk.Button(self, text="Назад", width=20, height=3,
                                     command=lambda: self.controller.show_frame(MAIN_FRAME_NAME))
        self.back_button.pack()

    def __add_quantity(self):
        quantity_name = self.quantity_name_entry.get()
        if quantity_name == "":
            showerror("Название величины", "Введите название величины")
            return

        if len(quantity_name) > 30:
            showerror("Длинное название", "Название величины может содержать не более 30 символов")
            return

        add_new_quantity(quantity_name)
        self.controller.show_frame(MAIN_FRAME_NAME)

    def render(self):
        self.clear()

    def clear(self):
        self.quantity_name_entry.delete(0, tk.END)
