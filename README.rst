===============
flake8-no-types
===============

.. image:: https://img.shields.io/pypi/v/flake8-no-types.svg
        :target: https://pypi.python.org/pypi/flake8-no-types

.. image:: https://img.shields.io/travis/adamchainz/flake8-no-types.svg
        :target: https://travis-ci.org/adamchainz/flake8-no-types

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/python/black

A `flake8 <https://flake8.readthedocs.io/en/latest/index.html>`_ plugin to ban
type hints.

This can be useful in code bases where you aren't running type checking (yet?)
but developers or their IDE's keep adding type hints that can end up being
incorrect.

Installation
------------

Install from ``pip`` with:

.. code-block:: sh

     pip install flake8-no-types

Python 3.5-3.8 supported.

When installed it will automatically be run as part of ``flake8``; you can
check it is being picked up with:

.. code-block:: sh

    $ flake8 --version
    3.7.9 (flake8-no-types: 1.0.0, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.8.0 on Darwin

Rules
-----

NT001: No type hints.
~~~~~~~~~~~~~~~~~~~~~

Complains about all forms of type hints:

* Function annotations: `def foo() -> int:`
* Variable hints: `foo: int = 1`
