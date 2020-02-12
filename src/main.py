import json
from model.quantity import *


def load_data():
    with open('../resources/quantities.json') as json_file:
        json_data = json.load(json_file)
        phys_quantities = []

        for quantities_json in json_data:
            phys_quantities.append(PhysicalQuantity.decode_from_json(quantities_json))

        return phys_quantities


if __name__ == "__main__":
    physical_quantities = load_data()
