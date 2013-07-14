Impyccable
==========

A python unit testing companion that generates a test dataset.

This project was inspired by quickcheck and its derivitives for functional 
programming languages and a dislike of the python alternatives.

Impyccable is meant to run along side any unit testing framework seamlessly.
One should simply write a test function and then decorate it by telling
Impyccable what kind of data you want to be given to the test function.

Unit testing with Impyccable will prevent testing your code against a small
set of specific values. This means that test code can be both thorough
and can also be more sucinct by stripping limited data set definitions.