Usage
=====

``Impyccable`` is designed for use with any unittesting framework. As such the
easiest way to begin using ``Impyccable`` is to decorate a unittesting
function with the structure of the required data set.

The following is a simple test from ``Impyccable`` itself that demonstrates
both methods of running Impyccable tests.

.. literalinclude:: ../test/test_runners.py
    :language: python
    :linenos:

Here you can see the recomended way of using the ``@Impyccable`` decorator on a
unittest function aswell as the functional approach of using a ``Runner``
object. By default these execute the underlying function with new data 10 times
but this can be changed with the ``runs`` argument. 

Both of these methods constructed with a definition of the kinds of data
generators that output the data you want to test against. These arguments are
to be used much the same as you would if you where calling the function with
real data but to instead have generators as values.

When a decorated function or a runner object is called it will instead run the
data tests without requiring any arguments in the call. Although the number of
runs can be defined here as well as in the decorator or ``Runner``construction.

There are multiple usefull :mod:"impyccable.generators" to use.
