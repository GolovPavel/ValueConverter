import json
from tkinter.messagebox import showwarning

from constants.files import QUANTITIES_FILE_PATH
from model.quantity import PhysicalQuantity


def add_new_quantity(quantity_name):
    physical_quantities = get_all_quantities()

    for quantity in physical_quantities:
        if quantity_name == quantity.name:
            showwarning("Величина существует", "Введенная величина уже существует")
            return

    new_quantity = PhysicalQuantity(quantity_name, [])
    physical_quantities.append(new_quantity)
    save_quantity(physical_quantities)


def save_quantity(quantities_list):
    result = []

    for quantity in quantities_list:
        var = quantity.__dict__
        for i in range(len(var['units'])):
            var['units'][i] = var['units'][i].__dict__
        result.append(var)

    with open(QUANTITIES_FILE_PATH, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, ensure_ascii=False)


def get_all_quantities():
    physical_quantities = []

    with open(QUANTITIES_FILE_PATH, encoding="utf-8") as json_file:
        json_data = json.load(json_file)

        for quantities_json in json_data:
            physical_quantity = PhysicalQuantity.decode_from_json(quantities_json)
            physical_quantities.append(physical_quantity)

    return physical_quantities
