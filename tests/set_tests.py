from mc import *
from nose.tools import eq_


def test_set_mk_string():
    eq_(Set([5, 6, 7]).mk_string("_", "<", ">"), "<5_6_7>")


def test_set_map():
    eq_(Set([5, 6, 7]).map(lambda x: x % 2), Set([1, 0]))


def test_set_filter():
    eq_(Set([5, 6, 7]).filter(lambda x: x % 2 == 0), Set([6]))


def test_set_flat_map():
    eq_(Set([1, 2]).flat_map(lambda x: (x * 2, x * 4)), {2, 4, 8})
