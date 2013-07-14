Impyccable
==========

A python unit testing companion that generates a test dataset.

This project was inspired by quickcheck and its derivitives for functional
programming languages and a dislike of the python alternatives.

Impyccable is meant to run along side any unit testing framework seamlessly.
One can simply write a function that takes your dataset and then a unit testing
function that gives impyccable your function and a definition of the kind of
data set you want to be given to the test function.

Unit testing with Impyccable will prevent testing your code against a small set
of specific values. This means that test code can be both thorough and can also
be more sucinct by stripping limited data set definitions.

While Impyccable is primarily designed for assisting with unit testing, it also
provides a capable set of random data generators that can be used on its own.
