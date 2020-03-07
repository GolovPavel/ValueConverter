class Unit:

    def __init__(self, name, is_base_unit, conversion_factor, conversion_operation):
        self.name = name
        self.is_base_unit = is_base_unit
        self.conversion_factor = conversion_factor
        self.conversion_operation = conversion_operation

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def decode_from_json(json_obj):
        return Unit(json_obj["name"], bool(json_obj["is_base_unit"]), float(json_obj["conversion_factor"]),
                    json_obj["conversion_operation"])
