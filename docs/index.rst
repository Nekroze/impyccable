.. Impyccable documentation master file, created by
   sphinx-quickstart on Mon Jul 15 12:04:36 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Impyccable's documentation!
======================================

A python unit testing companion that generates a test dataset.

This project was inspired by QuickCheck (and its derivitives for functional
programming languages) and the abondoned Python alternatives.

Impyccable is meant to run along side any unit testing framework seamlessly.

Unit testing with Impyccable will prevent testing your code against a small set
of specific values. This means that test code can be both thorough and succinct
by stripping limited data set definitions.

All you really need to do is decorate a test function with a general
definition of the data it expects and it will be generated for you at run time.

While Impyccable is primarily designed for assisting with unit testing, it also
provides a capable set of random data generators that can be used on its own.

Contents:

.. toctree::
   :maxdepth: 4

   usage
   runners
   generators


Feedback
========

If you have any suggestions or questions about ``Impyccable`` feel free to
email me at nekroze@eturnilnetwork.com.

You can check out more of what I am doing at http://nekroze.eturnilnetwork.com
my blog.

If you encounter any errors or problems with ``Impyccable``, please let me know!
Open an Issue at the GitHub http://github.com/Nekroze/impyccable main repository.
