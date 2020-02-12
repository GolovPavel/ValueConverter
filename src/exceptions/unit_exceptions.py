class NoBaseUnitException(Exception):

    def __init__(self, *args):
        if args:
            self.category = args[0]
        else:
            self.category = None

    def __str__(self):
        if self.category:
            return "Can't find base unit for category {}".format(self.category)
        else:
            return "Can't find base unit"
