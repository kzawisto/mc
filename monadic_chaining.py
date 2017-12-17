import copy
class List(list):
    def __init__(self, args=[]):
        super(List, self).__init__(args)
        
    def _map(self,func):
        l = []
        for i in self:
            l.append(func(i))
        return List(l)
    
    def _filter(self, func):
        l = []
        for i in self:
            if func(i):
                l.append(i)
        return List(l)
    def _fold(self, func, starts):
        v = copy.deepcopy(starts)
        for i in self:
            v = func(v,i)
        return v
    def _group_by(self, func):
        d = {}
        for i in self:
            val = func(i)
            if val not in d:
                d[val] = List()
            d[val].append(i)
        return Dic(d)

    def _foreach(self, func):
        for i in self:
            func(i)

    def _to_dict(self):
        return {i[0]:i[1] for i in self}

    def _mk_string(self, sep = ",", left = "", right = ""):
        return left + sep.join([str(i) for i in self]) + right

    def __add__(self, other):
        return List(self + other)
        
class Dic(dict):
    def __init__(self, args):
        super(Dic, self).__init__(args)
    def _map_vals(self, func):
        l = {}
        for i in self:
            l[i] = func(i, self[i])
        return Dic(l)
    def _map_keys(self, func):
        l = {}
        for i in self:
            l[func(i, self[i])] = self[i]
        return Dic(l)

    def _filter(self, func):
        l = {}
        for i in self:
            if func(i, self[i]):
               l[i] = self[i]
        return Dic(l)

    def get_or_else(self, key, else_val):
        if key in self:
            return self[key]
        else:
            return else_val

    @property
    def _to_list(self):
        return List([(i, self[i]) for i in self])

    def _foreach(self, func):
        for i in self:
            func(i, self[i])
