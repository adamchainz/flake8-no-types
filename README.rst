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

Unmaintained (2022-12-07)
-------------------------

I stopped maintaining this package as it has never been popular.
Also, it isn’t really practical to ban all type hints, since tools like ``dataclasses`` use them at runtime.

----

A `flake8 <https://flake8.readthedocs.io/en/latest/index.html>`_ plugin to ban type hints.

This can be useful in code bases where you aren't running type checking (yet?) but developers or their IDE's add type hints that can be incorrect.

Requirements
============

Python 3.7 to 3.11 supported.

Installation
============

First, install with ``pip``:

.. code-block:: sh

     python -m pip install flake8-no-types

Second, if you define Flake8’s ``select`` setting, add the ``NT`` prefix to it.
Otherwise, the plugin should be active by default.

----

**Linting a Django project?**
Check out my book `Boost Your Django DX <https://adamchainz.gumroad.com/l/byddx>`__ which covers Flake8 and many other code quality tools.

----

Rules
=====

NT001: No type hints.
---------------------

Flags all forms of type hints:

* Function annotations: `def foo() -> int:`
* Variable hints: `foo: int = 1`
