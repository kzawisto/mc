from mc import *
from nose.tools import eq_
from hamcrest import *


def test_set_mk_string():
    eq_(Set([5, 6, 7]).mk_string("_", "<", ">"), "<5_6_7>")


def test_set_map():
    eq_(Set([5, 6, 7]).map(lambda x: x % 2), Set([1, 0]))


def test_set_filter():
    eq_(Set([5, 6, 7]).filter(lambda x: x % 2 == 0), Set([6]))


def test_set_flat_map():
    eq_(Set([1, 2]).flat_map(lambda x: (x * 2, x * 4)), {2, 4, 8})


def test_set_addition_w_list():
    assert_that(
        Set([1]) + List(["3", 4]), equal_to(Set([1, "3", 4]))
    )


def test_set_addition_repeated_indices():
    assert_that(
        Set([1, 2]) + List(["3", 4, 2, 2]), equal_to(Set(["3", 4, 2, 1]))
    )
