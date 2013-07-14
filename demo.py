from impyccable.generators import Boolean
from impyccable.runner import Impyccable

@Impyccable(Boolean())
def test(val):
    print(val)

test(20)
