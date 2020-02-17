import json
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from model.quantity import *


class Application(tk.Frame):
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    def __init__(self, root):
        super().__init__(root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.root = root
        self.pack()

        self.__load_data()
        self.__init_base_window()
        self.__init_main_screen()

    def __load_data(self):
        """Load data about quantities and units from file resources/default_quantities.json"""
        with open('../resources/default_quantities.json') as json_file:
            json_data = json.load(json_file)
            self.phys_quantities = {}

            for quantities_json in json_data:
                physical_quantity = PhysicalQuantity.decode_from_json(quantities_json)
                self.phys_quantities[physical_quantity.name] = physical_quantity.units

    def __init_base_window(self):
        """Init base window parameters"""
        self.pack_propagate(0)
        root.title("Конвертер величин")

        # Set application window to center of the screen
        position_right = int(self.root.winfo_screenwidth() / 2 - self.WINDOW_WIDTH / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - self.WINDOW_HEIGHT / 2)
        root.geometry("+{}+{}".format(position_right, position_down))

    def __init_main_screen(self):
        """Init elements on the main screen of application"""
        self.main_label = tk.Label(self, text="Конвертер физических величин", font="Helvetica 30 bold")
        self.main_label.pack(pady=40)

        self.chose_quantity_label = tk.Label(self, text="Выберите физическую величину", font="Helvetica 20")
        self.chose_quantity_label.pack(pady=50)

        self.selected_quantity = tk.StringVar()
        self.quantity_selector = ttk.Combobox(self, values=list(self.phys_quantities.keys()), justify='center',
                                              textvariable=self.selected_quantity)
        self.quantity_selector['state'] = 'readonly'
        self.quantity_selector.pack()

        self.select_quantity_button = tk.Button(self, text="Выбор", width=20, height=3, command=self.__select_quantity)
        self.select_quantity_button.pack(pady=40)

    def __select_quantity(self):
        """Select quantity callback"""

        if self.selected_quantity.get() == "":
            showwarning("Выберите величину", "Выберите физическую величину")
            return

        # TODO add select quantity logic


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
