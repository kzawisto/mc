import re


class String(str):
    def __new__(cls, value):
        obj = super(String, cls).__new__(cls, value)
        return obj

    def strip_prefix(self, prefix):
        assert prefix == self[:len(prefix)], "{} is not prefix to {}".format(prefix, self)
        return self[len(prefix):]

    def strip_suffix(self, suffix):
        assert suffix == self[-len(suffix):], "{} is not prefix to {}".format(suffix, self)
        return self[:-len(suffix)]

    def search_regex(self, regex):
        match = re.search(regex, self)
        return match.group()
