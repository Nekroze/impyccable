"""Test runner."""
__author__ = 'Taylor "Nekroze" Lawson'
__email__ = 'nekroze@eturnilnetwork.com'


class _Arger(object):
    """
    Stores argument generators and when called returns a set of arguments from
    those generators.
    """
    def __init__(self, args, kwargs):
        self._args = args
        self._kwargs = kwargs

    def args(self):
        """
        Returns an argument list from stored generators.
        """
        return [next(arg) for arg in self._args]

    def kwargs(self):
        """
        Returns a keyword argument dictionary from stored generators.
        """
        return {kw: next(arg) for kw, arg in self._kwargs.items}


class Runner(object):
    """
    Stores a given function and argument generators to execute when asked.
    """
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = _Arger(args, kwargs)

    def call(self, runs=1):
        """
        Call the stored function with arguments pulled from generates with
        optional repetition.
        """
        for _ in range(runs):
            self.func(*self.args.args(), **self.args.kwargs())