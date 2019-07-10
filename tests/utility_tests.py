
from mc._list import List
from mc.utility import *
from hamcrest import *


def test_chaining_glues_callables():
    assert_that(
        List([1, 2, 3]).map(chain(lambda x: x*x, str, lambda y: "_" + y)),
        equal_to(List(["_1", "_4", "_9"]))
    )


def test_mux_multilexes_unnamed_callables():
    import math
    assert_that(
        mux(sum, lambda x: x[0])(List([1, 2, 3])),
        equal_to((6, 1))
    )


def test_mux_multilexes_unnamed_callables():
    import math
    assert_that(
        mux(sum=sum, maximum=max)(List([1, 2, 3])),
        equal_to(dict(sum=6, maximum=3))
    )


def test_addition():
    assert_that(List([1, 2, 4]).reduce(add).get(), equal_to(7))


def test_subtraction():
    assert_that(List([1, 2, 4]).fold(subtr, 100), equal_to(93))


def test_multiplication():
    assert_that(List([1, 2, 4]).reduce(multiply).get(), equal_to(8))
