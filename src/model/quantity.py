from exceptions.unit_exceptions import NoBaseUnitException


class PhysicalQuantity:

    def __init__(self, name, units):
        self.name = name
        self.units = units

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_base_unit(self):
        for unit in self.units:
            if unit.is_base_unit:
                return unit

        raise NoBaseUnitException(self.name)

    @staticmethod
    def decode_from_json(json_obj):
        json_units = json_obj["units"]
        units = []

        for unit in json_units:
            units.append(Unit.decode_from_json(unit))

        return PhysicalQuantity(json_obj["name"], units)


class Unit:

    def __init__(self, name, is_base_unit, conversion_factor):
        self.name = name
        self.is_base_unit = is_base_unit
        self.conversion_factor = conversion_factor

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def decode_from_json(json_obj):
        return Unit(json_obj["name"], bool(json_obj["is_base_unit"]), json_obj["conversion_factor"])
