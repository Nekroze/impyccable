from impyccable.generators import *
from impyccable.runners import Impyccable
import string


TEST_RUNS = 100


@Impyccable(Value(5), runs=TEST_RUNS)
def test_Value(val):
    assert val == 5


@Impyccable(Choice([2,3,4]), runs=TEST_RUNS)
def test_Float(val):
    assert val in [2,3,4]


@Impyccable(String(0, 10, string.lowercase), runs=TEST_RUNS)
def test_String(val):
    assert 0 <= len(val) <= 10
    for char in val:
        assert char in string.lowercase


@Impyccable(Integer(0, 10), runs=TEST_RUNS)
def test_Integer(val):
    assert 0 <= val <= 10


@Impyccable(Float(0, 10), runs=TEST_RUNS)
def test_Float(val):
    assert 0 <= val <= 10


@Impyccable(Boolean(), runs=TEST_RUNS)
def test_Boolean(val):
    assert val is True or val is False


@Impyccable(List(Value(5), 5, 5), runs=TEST_RUNS)
def test_List(val):
    assert val == [5,5,5,5,5]


@Impyccable(Tuple(Boolean(), Integer()), runs=TEST_RUNS)
def test_Tuple(val):
    assert len(val) == 2
    assert isinstance(val[0], bool)
    assert isinstance(val[1], int)


@Impyccable(Dictionary({"a": Boolean(), "z": String()}), runs=TEST_RUNS)
def test_Dictionary(val):
    assert "a" in val
    assert isinstance(val["a"], bool)
    assert "z" in val
    assert isinstance(val["z"], str)
