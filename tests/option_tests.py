from hamcrest import *
from mc import *


def test_nothing_should_equal_nothing():
    assert_that(
        Nothing(), equal_to(Nothing())
    )


def test_nothing_should_not_equal_some():
    assert_that(
        Nothing(), not_(equal_to(Some(3)))
    )


def test_some_should_not_equal_nothing():
    assert_that(
        Some(4), not_(equal_to(Nothing()))
    )


def test_some_equality_should_compare_values():
    assert_that(
        Some("hello"), not_(equal_to(Some("world")))
    )
    assert_that(
        Some(4), equal_to(Some(4))
    )


def test_some_should_map_to_some():
    assert_that(Some(10).map(lambda x: 10 * x), equal_to(Some(100)))


def test_some_should_flat_map_to_some():
    assert_that(Some(10).flat_map(lambda x: Some(10 * x)), equal_to(Some(100)))


def test_some_should_flat_map_to_nothing():
    assert_that(Some(10).flat_map(lambda x: Nothing()), equal_to(Nothing()))


def test_get_on_nothing_throws():
    assert_that(calling(lambda: Nothing().get()), raises(AttributeError))


def test_get_on_some_extracts_value():
    assert_that(calling(lambda: Some(10).get())(), equal_to(10))


def test_get_or_else_on_nothing_should_return_else_val():
    assert_that(Nothing().get_or_else(10), equal_to(10))


def test_get_or_else_on_some_should_return_value():
    assert_that(Some(13).get_or_else(10), equal_to(13))


def test_get_or_else_lazy_on_some_should_return_value_and_dont_call_function():
    assert_that(Some(13).get_or_else_lazy(
        lambda: raise_(AttributeError(""))), equal_to(13))


def test_get_or_else_lazy_on_nothing_call_function():
    assert_that(
        Nothing().get_or_else_lazy(lambda: 10), equal_to(10)
    )


def test_nothing_should_work_as_iterable():
    assert_that(
        [k for k in Nothing()], empty()
    )


def test_some_should_work_as_iterable():
    assert_that(
        [k for k in Some(3)], contains(3)
    )
