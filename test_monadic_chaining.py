from monadic_chaining import *

def test_list_map():
    assert List([1, 2, 3]).map(lambda x: x * 2)==[2,4,6]