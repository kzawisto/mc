class Set(set):
    def __init__(self, args={}):
        super(Set, self).__init__(args)

    def map(self, func):
        return Set([func(item) for item in self])

    def flat_map(self, func):
        return Set([r for item in self for r in func(item)])

    def filter(self, func):
        return Set([item for item in self if func(item)])

    def to_dict(self):
        from mc.dict import Dict
        return Dict({item[0]: item[1] for item in self})

    def to_list(self):
        from mc.list import List
        return List(self)

    def mk_string(self, sep=", ", left="", right=""):
        return self.to_list().sorted().mk_string(sep, left, right)

    def __add__(self, other):
        return Set(list(self) + list(other))
