from impyccable.generators import List, Integer
from impyccable.runners import Impyccable, Runner

print("===\nDecorator\n===")
@Impyccable(List(bool))
def test(val):
    """
    This function takes a list of booleans.
    """
    print(val)

test(runs=5)

print("===\nRunner\n===")
def test2(val):
    """
    The runner will supply test2 with randomly generated integers.
    """
    print(val)

imptest = Runner(test2, Integer())
imptest(5)
