from unittest import TestCase
from impyccable.generators import *
from impyccable.runners import Impyccable


TEST_RUNS = 1000


class GeneratorTests(TestCase):

    @Impyccable(Value(5), runs=TEST_RUNS)
    def test_Value(self, val):
        self.assertEqual(val, 5)

    @Impyccable(Function(lambda : 10), runs=TEST_RUNS)
    def test_Value(self, val):
        self.assertEqual(val, 10)


    @Impyccable(Choice([2,3,4]), runs=TEST_RUNS)
    def test_Float(self, val):
        self.assertIn(val, [2,3,4])


    @Impyccable(String(0, 10, "abcdefghijklmnopqrstuvwxyz"), runs=TEST_RUNS)
    def test_String(self, val):
        self.assertTrue(0 <= len(val) <= 10)
        for char in val:
            self.assertTrue(char.islower())


    @Impyccable(Words(2, 2, 4, 4, "abcdefghijklmnopqrstuvwxyz"), runs=TEST_RUNS)
    def test_Words(self, val):
        words = val.split(' ')
        self.assertEqual(len(words), 4)

        for word in words:
            self.assertTrue(word.islower())
            self.assertEqual(len(word), 2)


    @Impyccable(Integer(0, 10), runs=TEST_RUNS)
    def test_Integer(self, val):
        self.assertTrue(0 <= val <= 10)


    @Impyccable(Float(0, 10), runs=TEST_RUNS)
    def test_Float(self, val):
        self.assertTrue(0 <= val <= 10)


    @Impyccable(Boolean(), runs=TEST_RUNS)
    def test_Boolean(self, val):
        self.assertIn(val, (True, False))


    @Impyccable(List(Value(5), 5, 5), runs=TEST_RUNS)
    def test_List(self, val):
        self.assertEqual(val, [5,5,5,5,5])


    @Impyccable(Tuple(Boolean(), Integer()), runs=TEST_RUNS)
    def test_Tuple(self, val):
        self.assertEqual(len(val), 2)
        self.assertIsInstance(val[0], bool)
        self.assertIsInstance(val[1], int)


    @Impyccable(Dictionary({"a": Boolean(), "z": String()}), runs=TEST_RUNS)
    def test_Dictionary(self, val):
        self.assertIn("a", val)
        self.assertIsInstance(val["a"], bool)
        self.assertIn("z", val)
        self.assertIsInstance(val["z"], str)


    #@Impyccable(Typer(str, int, float, bool), runs=TEST_RUNS)
    def test_Typer(self, string, integer, floating, boolean):
        self.assertTrue(string.isprintable())
        self.assertIsInstance(integer, int)
        self.assertIsInstance(floating, float)
        self.assertIsInstance(boolean, bool)
