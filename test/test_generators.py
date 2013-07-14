from impyccable.generators import *
from impyccable.runners import Impyccable


@Impyccable(Value(5))
def test_Value(val):
    assert val == 5
