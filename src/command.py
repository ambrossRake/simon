class Command:

    def __init__(self, name, description, func, alias):
        self.name = name
        self.description = description
        self.func = func
        self.alias = alias

    def execute(self, args):
        self.func(args)
