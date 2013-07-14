from impyccable.generators import *
from impyccable.runners import Impyccable
import string


@Impyccable(Value(5), runs=100)
def test_Value(val):
    assert val == 5


@Impyccable(String(0, 10, string.lowercase), runs=100)
def test_String(val):
    assert 0 <= len(val) <= 10
    for char in val:
        assert char in string.lowercase
