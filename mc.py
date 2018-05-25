import copy
class List(list):
    def __init__(self, args=[]):
        super(List, self).__init__(args)
        
    def map(self,func):
        l = []
        for i in self:
            l.append(func(i))
        return List(l)

    def flat_map(self,func):
        l = []
        for i in self:
            result = func(i)
            for r in result:
                l.append(r)
        return List(l)
    
    def filter(self, func):
        l = []
        for i in self:
            if func(i):
                l.append(i)
        return List(l)

    def fold(self, func, starts):
        v = copy.deepcopy(starts)
        for i in self:
            v = func(v,i)
        return v

    def group_by(self, func):
        d = {}
        for i in self:
            val = func(i)
            if val not in d:
                d[val] = List()
            d[val].append(i)
        return Dic(d)

    def foreach(self, func):
        for i in self:
            func(i)

    def sorted(self, key = None):
        return List(sorted(self, key=key))

    def to_dict(self):
        return Dic({i[0]:i[1] for i in self})

    def to_set(self):
        return Set(self)

    def mk_string(self, sep = ", ", left = "", right = ""):
        return left + sep.join([str(i) for i in self]) + right

    def __add__(self, other):
        return List(self + other)

class Set(set):
    def __init__(self, args={}):
        super(Set, self).__init__(args)

    def map(self,func):
        l = set()
        for i in self:
            l.add(func(i))
        return Set(l)

    def flat_map(self,func):
        l = set()
        for i in self:
            result = func(i)
            for r in result:
                l.add(r)
        return Set(l)

    def filter(self, func):
        l = set()
        for i in self:
            if func(i):
                l.add(i)
        return Set(l)

    def to_dict(self):
        return Dic({i[0]:i[1] for i in self})

    def to_list(self):
        return List(self)

    def mk_string(self, sep = ", ", left = "", right = ""):
        return left + sep.join([str(i) for i in self]) + right

class Dic(dict):
    def __init__(self, args):
        super(Dic, self).__init__(args)
    def map_vals(self, func):
        l = {}
        for i in self:
            l[i] = func(i, self[i])
        return Dic(l)
    def map_keys(self, func):
        l = {}
        for i in self:
            l[func(i, self[i])] = self[i]
        return Dic(l)

    def filter(self, func):
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

    def with_kv(self, key, value):
        new_dic = copy.copy(self)
        new_dic[key] = value
        return new_dic

    def with_dic(self, dic):
        new_dic = copy.copy(self)
        for key in dic:
            new_dic[key] = dic[key]
        return new_dic

    @property
    def to_list(self):
        return List([(i, self[i]) for i in self])

    def foreach(self, func):
        for i in self:
            func(i, self[i])

class Option(object):
    def __init__(self):
        pass

    def is_none(self):
        pass

    def flat_map(self, func):
        pass

    def map(self, func):
        pass

    def get(self):
        pass

    def get_or_else(self, other):
        pass

    def get_or_else_lazy(self, func):
        pass


class Nothing(Option):
    def __init__(self):
        super(Nothing, self).__init__()

    def is_none(self):
        return True

    def flat_map(self, func):
        return self

    def map(self, func):
        return self

    def get(self):
        raise AttributeError("get called on option's None")

    def get_or_else(self, other):
        return other

    def get_or_else_lazy(self, func):
        return func()

class Some(Option):
    def __init__(self, value):
        super(Some, self).__init__()
        self.value = value

    def is_none(self):
        return False

    def flat_map(self, func):
        return func(self.value)

    def map(self, func):
        return Some(func(self.value))

    def get(self):
        return self.value

    def get_or_else(self, func):
        return self.value

    def get_or_else_lazy(self, func):
        return self.value

class Try(object):
    def __init__(self):
        pass

    def is_failure(self):
        pass

    def is_success(self):
        pass

    def flat_map(self, func):
        pass

    def map(self, func):
        pass

    def get(self):
        pass

    def get_or_else(self, func):
        pass

class Failure(Try):
    def __init__(self, exception):
        super(Failure, self).__init__()
        self.exception = exception

    def is_failure(self):
        return True

    def is_success(self):
        return False

    def flat_map(self, func):
        return self

    def map(self, func):
        return self

    def result(self):
        raise AttributeError("result called on Try's Failure")

    def get_or_else(self, other):
        return other

    def to_list(self):
        return List()

class Success(Try):
    def __init__(self, value):
        super(Success, self).__init__()
        self.value = value

    def is_failure(self):
        return False

    def is_success(self):
        return True

    def flat_map(self, func):
        try:
            return func(self.value)
        except Exception as e:
            return Failure(e)

    def map(self, func):
        try:
            return Success(func(self.value))
        except Exception as e:
            return Failure(e)

    def result(self):
        raise AttributeError("result called on Try's Failure")

    def get_or_else(self, other):
        return self.value

    def to_list(self):
        return List(self.value)

        
