from mc import *
from nose.tools import eq_


def test_list_map():
    eq_(List([1, 2, 3]).map(lambda x: x * 2), [2,4,6])


def test_list_filter():
    eq_(List([1, 2, 3]).filter(lambda x: x < 2), [1])


def test_list_fold():
    eq_(List([1, 2, 3]).fold(lambda x, y: x * y, 1), 6)


def test_list_group_by():
    eq_(
        List([1, 2, 3, 4, 5, 6]).group_by(lambda x: x % 2),
        {1: [1,3,5], 0: [2, 4, 6]}
    )


def test_list_mk_string():
    eq_( List([5, 6, 7]).mk_string("_", "<", ">"), "<5_6_7>")


def test_list_to_dict():
    eq_( List([(5, 6), (7, 8)]).to_dict(), {5: 6, 7: 8})

def test_list_to_set():
    eq_(List([5,6,7]).to_set().to_list(),List([5,6,7]) )

def test_set_map():
    eq_(Set([5,6,7]).map(lambda x: x % 2), Set([1,0]) )

def test_set_filter():
    eq_(Set([5,6,7]).filter(lambda x: x % 2==0), Set([6]) )

def test_dict_map_keys():
    eq_(Dic({1: 5, 2: 6}).map_keys(lambda x,y: x * y), {5: 5, 12: 6})


def test_dict_map_vals():
    eq_(Dic({1: 5, 2: 6}).map_vals(lambda x,y: x + y), {1: 6, 2: 8})


def test_dict_filter():
    eq_(
        Dic({1: 5, 2: 6, 4: 4}).filter(lambda x,y: y < 6 and x < 2),
        {1: 5}
    )

def test_get_or_else():
    dictionary = Dic({1: 2, 3: 4})
    eq_(dictionary.get_or_else(1, 0), 2)
    eq_(dictionary.get_or_else(2, 10), 10)

def test_dic_with_kv():
    dictionary = Dic({1: 2, 3: 4})
    eq_(dictionary.with_kv(4,5), Dic({1:2, 3:4, 4:5}))
    eq_(dictionary, Dic({1:2, 3:4}))

def test_dic_with_dic():
    dictionary = Dic({1: 2, 3: 4})
    eq_(dictionary.with_dic({4:5, 6:7}), Dic({1:2, 3:4, 4:5, 6:7}))
    eq_(dictionary, Dic({1:2, 3:4}))

def test_list_multiproc_map():
    def process_el(x):
        return x * 2
    eq_(List([1, 2, 3]).multiproc_map(process_el), [2,4,6])