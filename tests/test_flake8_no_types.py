import re
import sys
from textwrap import dedent

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


def test_version(flake8_path):
    result = flake8_path.run_flake8(["--version"])
    version_regex = r"flake8-no-types:( )*" + version("flake8-no-types")
    unwrapped = "".join(result.out_lines)
    assert re.search(version_regex, unwrapped)


# NT001


def test_NT001_pass_variable(flake8_path):
    (flake8_path / "example.py").write_text("foo = 1\n")
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NT001_pass_function(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo():
                pass
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == []


def test_NT001_fail_variable_declaration(flake8_path):
    (flake8_path / "example.py").write_text("foo: int = 1\n")
    result = flake8_path.run_flake8()
    assert result.out_lines == ["./example.py:1:1: NT001 No type hints."]


def test_NT001_fail_class_variable_declaration(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            class Foo:
                bar: int
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == ["./example.py:2:5: NT001 No type hints."]


def test_NT001_fail_function_arguments(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo(x: int):
                return x * 2
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == ["./example.py:1:9: NT001 No type hints."]


def test_NT001_fail_function_keyword_arguments(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo(x: int = 1):
                return x * 2
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == ["./example.py:1:9: NT001 No type hints."]


def test_NT001_fail_function_return(flake8_path):
    (flake8_path / "example.py").write_text(
        dedent(
            """\
            def foo() -> int:
                return 2
            """
        )
    )
    result = flake8_path.run_flake8()
    assert result.out_lines == ["./example.py:1:1: NT001 No type hints."]
