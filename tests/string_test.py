from hamcrest import *
from mc.string import String


def test_string_should_strip_prefix():
    assert_that(String("abc").strip_prefix("a"), equal_to("bc"))
    assert_that(String("abc").strip_prefix("abc"), equal_to(""))
    assert_that(String("abc").strip_prefix(""), equal_to("abc"))


def test_string_should_throw_on_strip_prefix_if_arg_is_no_prefix():
    assert_that(calling(lambda: String("abc").strip_prefix("c")),
                raises(AssertionError))


def test_string_should_have_str_attr():
    assert_that(String("abc").upper(), equal_to("ABC"))
