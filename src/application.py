import tkinter as tk
import os
import util

from frames.add_quantity_frame import AddQuantityFrame
from frames.converter_frame import ConverterFrame
from frames.main_frame import MainFrame
from util import get_all_quantities
from constants.files import *


class Application(tk.Tk):
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.__init_base_params()
        self.__create_db()
        self.__load_data()

        self.selected_quantity = tk.StringVar()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ConverterFrame, AddQuantityFrame, MainFrame):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainFrame.__name__)

    def show_frame(self, page_name):
        self.__load_data()
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

    def __create_db(self):
        if os.path.isfile(QUANTITIES_FILE_PATH):
            return

        util.set_default_quantities()

    def __load_data(self):
        self.phys_quantities = {}
        all_quantities = get_all_quantities()
        for quantity in all_quantities:
            self.phys_quantities[quantity.name] = quantity.units
