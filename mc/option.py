class Option(object):
    def __init__(self):
        pass

    def __iter__(self):
        return []

    def is_none(self):
        return False

    def flat_map(self, func):
        return self

    def map(self, func):
        return self

    def get(self):
        pass

    def get_or_else(self, other):
        return other

    def get_or_else_lazy(self, func):
        return func()


class Nothing(Option):
    def __init__(self):
        super(Nothing, self).__init__()

    def __iter__(self):
        return iter([])

    def __str__(self):
        return "Nothing()"

    def is_none(self):
        return True

    def __eq__(self, other):
        return isinstance(self, other.__class__)

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

    def __iter__(self):
        return iter([self.value])

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.value == other.value
        return False

    def is_none(self):
        return False

    def __str__(self):
        return "Some({})".format(self.value)

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
