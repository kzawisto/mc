class Set(set):
    def __init__(self, args={}):
        super(Set, self).__init__(args)

    def map(self, func):
        new_set = set()
        for item in self:
            new_set.add(func(item))
        return Set(new_set)

    def flat_map(self, func):
        new_set = set()
        for item in self:
            result = func(item)
            for r in result:
                new_set.add(r)
        return Set(new_set)

    def filter(self, func):
        new_set = set()
        for item in self:
            if func(item):
                new_set.add(item)
        return Set(new_set)

    def to_dict(self):
        from mc.dict import Dict
        return Dict({item[0]: item[1] for item in self})

    def to_list(self):
        from mc.list import List
        return List(self)

    def mk_string(self, sep=", ", left="", right=""):
        return self.to_list().sorted().mk_string(sep, left, right)
