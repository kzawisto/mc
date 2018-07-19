from mc import List
from hamcrest import *
from nose.tools import eq_



def test_list_map():
    eq_(List([1, 2, 3]).map(lambda x: x * 2), [2, 4, 6])


def test_list_flat_map():
    eq_(List([1, 3]).flat_map(lambda x: (x * 2, x * 4)), [2, 4, 6, 12])


def test_list_filter():
    eq_(List([1, 2, 3]).filter(lambda x: x < 2), [1])


def test_list_fold():
    eq_(List([1, 2, 3]).fold(lambda x, y: x * y, 1), 6)


def test_list_group_by():
    eq_(
        List([1, 2, 3, 4, 5, 6]).group_by(lambda x: x % 2),
        {1: [1, 3, 5], 0: [2, 4, 6]}
    )


def test_list_mk_string():
    eq_(List([5, 6, 7]).mk_string("_", "<", ">"), "<5_6_7>")


def test_list_to_dict():
    eq_(List([(5, 6), (7, 8)]).to_dict(), {5: 6, 7: 8})


def test_list_to_set():
    eq_(List([5, 6, 7]).to_set().to_list(), List([5, 6, 7]))


def test_list_foreach():
    dictionary = {}

    def add_to_dict(value):
        dictionary[value] = value

    List([9, 8, 7]).foreach(add_to_dict)
    actual = set(dictionary.keys())
    eq_(actual, {9, 8, 7})


def test_list_should_flat_map_iterables():
    assert_that(
        List([1, 2]).flat_map(lambda x: {x, x * 2, x * 3}), contains_inanyorder(1, 2, 3, 2, 4, 6)
    )
