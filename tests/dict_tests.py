from mc import Dict, List, Some, Nothing
from nose.tools import eq_
from hamcrest import *


def test_dict_map_keys():
    eq_(Dict({1: 5, 2: 6}).map_keys(lambda x, y: x * y), {5: 5, 12: 6})


def test_dict_map_vals():
    eq_(Dict({1: 5, 2: 6}).map_vals(lambda x, y: x + y), {1: 6, 2: 8})


def test_dict_filter():
    eq_(
        Dict({1: 5, 2: 6, 4: 4}).filter(lambda x, y: y < 6 and x < 2),
        {1: 5}
    )


def test_dict_get_or_else():
    dictionary = Dict({1: 2, 3: 4})
    eq_(dictionary.get_or_else(1, 0), 2)
    eq_(dictionary.get_or_else(2, 10), 10)


def test_dict_with_kv():
    dictionary = Dict({1: 2, 3: 4})
    eq_(dictionary.with_kv(4, 5), Dict({1: 2, 3: 4, 4: 5}))
    eq_(dictionary, Dict({1: 2, 3: 4}))


def test_dict_with_dic():
    dictionary = Dict({1: 2, 3: 4})
    eq_(dictionary.with_dic({4: 5, 6: 7}), Dict({1: 2, 3: 4, 4: 5, 6: 7}))
    eq_(dictionary, Dict({1: 2, 3: 4}))


def test_dict_mk_string():
    eq_(Dict({1: 2, 3: 4}).mk_string(" b ", "a", "<", ">"), "<1a2 b 3a4>")


def test_dict_get_should_throw_if_no_such_key():
    assert_that(calling(lambda: Dict({}).get("key")), raises(AssertionError))


def test_dict_get_should_fetch_value():
    assert_that(Dict({"key": 10}).get("key"), equal_to(10))


def test_dict_get_optional_should_return_nothing_if_no_such_key():
    assert_that(Dict({"key": 10}).get_optional("other"), instance_of(Nothing))


def test_dict_get_optional_should_return_value_in_some():
    assert_that(Dict({"key": 10}).get_optional("key"), Some(10))

def test_dict_adding_dicts():
    assert_that(Dict(dict(key=10)) + Dict(dict(key2=11)), equal_to( Dict(dict(key = 10, key2=11)))) 

def test_dict_adding_dict_to_list():
    assert_that(Dict(dict(key=10)) + List([("hello","world")]), equal_to( Dict(dict(key = 10, hello="world")))) 

