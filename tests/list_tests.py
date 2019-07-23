from hamcrest import *
from nose.tools import eq_
from mc import List, Some, Nothing,add


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


def test_list_multiproc_map():
    def process_el(x):
        return x * 2
    eq_(List([1, 2, 3]).multiproc_map(process_el), [2, 4, 6])


def test_list_foreach():
    dictionary = {}

    def add_to_dict(value):
        dictionary[value] = value

    List([9, 8, 7]).foreach(add_to_dict)
    actual = set(dictionary.keys())
    eq_(actual, {9, 8, 7})


def test_list_should_flat_map_iterables():
    assert_that(
        List([1, 2]).flat_map(lambda x: {
            x, x * 2, x * 3}), contains_inanyorder(1, 2, 3, 2, 4, 6)
    )


def test_list_reduce_should_return_nothing_for_empty_list():
    assert_that(
        List([]).reduce(lambda x, y: x), equal_to(Nothing())
    )


def test_list_reduce_should_aggregate_values():
    assert_that(
        List([1, 2, 3]).reduce(lambda x, y: x + y), equal_to(Some(6))
    )


def test_list_addition():
    assert_that(
        List([1, 2]) + List(["3", 4]), equal_to(List([1, 2, "3", 4]))
    )

def test_zip_with_idx():

    assert_that(
        List(["A","C","D"]).zip_with_idx(), equal_to(List([(0,"A"),(1,"C"),(2,"D")]))
    )

def test_list_pick_one():
    assert_that(
        calling(List(['1','2']).pick_one), raises(AssertionError)
    )   

    assert_that(
            calling(List([]).pick_one), raises(AssertionError)
    )   

    assert_that(
            List([1]).pick_one(), equal_to(1)
    )   

def test_accumulate():
    assert_that(
        List([1,2,3]).accumulate(add, 2), equal_to(8)
    )

def test_accumulate():
    assert_that(
        List([1,2,3]).accumulate(add, 2), equal_to(8)
    )

def test_count():
    assert_that(
        List([1,2,3]).count(), equal_to(3)
            )

def test_zip():

    assert_that(
    List([1,2]).zip([3,4]) , equal_to([(1,3),(2,4)])
    )

def test_zip_shift():

    assert_that(
    List([1,2]).zip_shift() , equal_to([(1,2)])
    )

    assert_that(
    List([1,2]).zip_shift(2) , equal_to([])
    )
    assert_that(
    List([1,2,3]).zip_shift(2) , equal_to([(1,3)])
    )
    assert_that(
    List([1,2,3]).zip_shift(1) , equal_to([(1,2),(2,3)])
    )
