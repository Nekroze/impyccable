from impyccable.generators import Boolean, Integer
from impyccable.runner import Impyccable, Runner

print("===\nDecorator\n===")
@Impyccable(Boolean())
def test(val):
    print(val)

test(5)

print("===\nRunner\n===")
def test2(val):
    print(val)

imptest = Runner(test2, Integer())
imptest(5)
