class Attempt(object):
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


class Failure(Attempt):
    def __init__(self, exception):
        super(Failure, self).__init__()
        self.exception = exception

    def is_failure(self):
        return True

    def __iter__(self):
        return []

    def is_success(self):
        return False

    def flat_map(self, func):
        return self

    def map(self, func):
        return self

    def result(self):
        raise AttributeError("result called on Attemt's Failure")

    def get_or_else(self, other):
        return other

    def to_list(self):
        from mc.list import List
        return List()


class Success(Attempt):
    def __init__(self, value):
        super(Success, self).__init__()
        self.value = value

    def is_failure(self):
        return False

    def __iter__(self):
        return [self.value]

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
        from mc.list import List
        return List(self.value)
