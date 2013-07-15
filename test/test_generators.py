from impyccable.generators import *
from impyccable.runners import Impyccable
import unittest


TEST_RUNS = 1000


class GeneratorTests(unittest.TestCase):

    @Impyccable(Value(5), runs=TEST_RUNS)
    def test_Value(self, val):
        assert val == 5


    @Impyccable(Choice([2,3,4]), runs=TEST_RUNS)
    def test_Float(self, val):
        assert val in [2,3,4]


    @Impyccable(String(0, 10, "abcdefghijklmnopqrstuvwxyz"), runs=TEST_RUNS)
    def test_String(self, val):
        assert 0 <= len(val) <= 10
        for char in val:
            assert char.islower()


    @Impyccable(Integer(0, 10), runs=TEST_RUNS)
    def test_Integer(self, val):
        assert 0 <= val <= 10


    @Impyccable(Float(0, 10), runs=TEST_RUNS)
    def test_Float(self, val):
        assert 0 <= val <= 10


    @Impyccable(Boolean(), runs=TEST_RUNS)
    def test_Boolean(self, val):
        assert val is True or val is False


    @Impyccable(List(Value(5), 5, 5), runs=TEST_RUNS)
    def test_List(self, val):
        assert val == [5,5,5,5,5]


    @Impyccable(Tuple(Boolean(), Integer()), runs=TEST_RUNS)
    def test_Tuple(self, val):
        assert len(val) == 2
        assert isinstance(val[0], bool)
        assert isinstance(val[1], int)


    @Impyccable(Dictionary({"a": Boolean(), "z": String()}), runs=TEST_RUNS)
    def test_Dictionary(self, val):
        assert "a" in val
        assert isinstance(val["a"], bool)
        assert "z" in val
        assert isinstance(val["z"], str)


if __name__ == '__main__':
        unittest.main()
