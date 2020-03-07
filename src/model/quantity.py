from model.unit import Unit


class PhysicalQuantity:

    def __init__(self, name, units):
        self.name = name
        self.units = units

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def decode_from_json(json_obj):
        json_units = json_obj["units"]
        units = []

        for unit in json_units:
            units.append(Unit.decode_from_json(unit))

        return PhysicalQuantity(json_obj["name"], units)