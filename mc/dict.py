import copy


class Dict(dict):
    def __init__(self, args):
        super(Dict, self).__init__(args)

    def map_vals(self, func):
        new_dict = {}
        for key in self:
            new_dict[key] = func(key, self[key])
        return Dict(new_dict)

    def map_keys(self, func):
        new_dict = {}
        for key in self:
            new_dict[func(key, self[key])] = self[key]
        return Dict(new_dict)

    def vals(self):
        from mc.list import List
        return List([self[key] for key in self])

    def keys(self):
        from mc.list import List
        return List([key for key in self])

    def to_list(self):
        from mc.list import List
        return List([(key, self[key]) for key in self])

    def filter(self, func):
        new_dict = {}
        for key in self:
            if func(key, self[key]):
                new_dict[key] = self[key]
        return Dict(new_dict)

    def get(self, key):
        assert key in self, "{} not in {}".format(key, self)
        return self[key]

    def get_optional(self, key):
        if key in self:
            from mc.option import Some
            return Some(self[key])
        else:
            from mc.option import Nothing
            return Nothing()

    def get_or_else(self, key, else_val):
        if key in self:
            return self[key]
        else:
            return else_val

    def with_kv(self, key, value):
        new_dict = copy.copy(self)
        new_dict[key] = value
        return new_dict

    def with_dic(self, dic):
        new_dict = copy.copy(self)
        for key in dic:
            new_dict[key] = dic[key]
        return new_dict

    def mk_string(self, pair_sep=",", kv_sep=",", left="{", right="}"):
        return \
            self.map_vals(lambda k, v: "{}{}{}".format(k, kv_sep, v)) \
                .vals().sorted() \
                .mk_string(pair_sep, left, right)

    def __str__(self):
        return "Dict" + self.mk_string()
