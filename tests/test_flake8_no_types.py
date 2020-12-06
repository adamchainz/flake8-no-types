import re
import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


def test_version(flake8dir):
    result = flake8dir.run_flake8(["--version"])
    version_regex = r"flake8-no-types:( )*" + version("flake8-no-types")
    unwrapped = "".join(result.out_lines)
    assert re.search(version_regex, unwrapped)


# NT001


def test_NT001_pass_variable(flake8dir):
    flake8dir.make_example_py("foo = 1")
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_NT001_pass_function(flake8dir):
    flake8dir.make_example_py(
        """
        def foo():
            pass
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == []


def test_NT001_fail_variable_declaration(flake8dir):
    flake8dir.make_example_py("foo: int = 1")
    result = flake8dir.run_flake8()
    assert result.out_lines == ["./example.py:1:1: NT001 No type hints."]


def test_NT001_fail_class_variable_declaration(flake8dir):
    flake8dir.make_example_py(
        """
        class Foo:
            bar: int
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == ["./example.py:2:5: NT001 No type hints."]


def test_NT001_fail_function_arguments(flake8dir):
    flake8dir.make_example_py(
        """
        def foo(x: int):
            return x * 2
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == ["./example.py:1:9: NT001 No type hints."]


def test_NT001_fail_function_keyword_arguments(flake8dir):
    flake8dir.make_example_py(
        """
        def foo(x: int = 1):
            return x * 2
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == ["./example.py:1:9: NT001 No type hints."]


def test_NT001_fail_function_return(flake8dir):
    flake8dir.make_example_py(
        """
        def foo() -> int:
            return 2
        """
    )
    result = flake8dir.run_flake8()
    assert result.out_lines == ["./example.py:1:1: NT001 No type hints."]
