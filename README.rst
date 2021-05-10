===============
flake8-no-types
===============

.. image:: https://img.shields.io/github/workflow/status/adamchainz/flake8-no-types/CI/main?style=for-the-badge
   :target: https://github.com/adamchainz/flake8-no-types/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/flake8-no-types.svg?style=for-the-badge
   :target: https://pypi.org/project/flake8-no-types/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

A `flake8 <https://flake8.readthedocs.io/en/latest/index.html>`_ plugin to ban type hints.

This can be useful in code bases where you aren't running type checking (yet?) but developers or their IDE's add type hints that can be incorrect.

Requirements
============

Python 3.6 to 3.10 supported.

Installation
============

First, install with ``pip``:

.. code-block:: sh

     python -m pip install flake8-no-types

Second, check that ``flake8`` lists the plugin in its version line:

.. code-block:: sh

    $ flake8 --version
    3.7.9 (flake8-no-types: 1.0.0, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.8.0 on Darwin

Third, add the ``NT`` prefix to your `select list <https://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-select>`__.
For example, if you have your configuration in ``setup.cfg``:

.. code-block:: ini

    [flake8]
    select = E,F,W,NT

----

**Linting a Django project?**
Check out my book `Speed Up Your Django Tests <https://gumroad.com/l/suydt>`__ which covers loads of best practices so you can write faster, more accurate tests.

----

Rules
=====

NT001: No type hints.
---------------------

Flags all forms of type hints:

* Function annotations: `def foo() -> int:`
* Variable hints: `foo: int = 1`
