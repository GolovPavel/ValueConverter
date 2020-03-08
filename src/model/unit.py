class Unit:

    def __init__(self, name, conversion_factor, conversion_operation):
        self.name = name
        self.conversion_factor = conversion_factor
        self.conversion_operation = conversion_operation

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def decode_from_json(json_obj):
        return Unit(json_obj["name"], float(json_obj["conversion_factor"]), json_obj["conversion_operation"])
