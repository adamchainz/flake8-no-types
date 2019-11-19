import ast
import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version


if sys.version_info >= (3, 6):
    AnnAssign = ast.AnnAssign
else:
    class AnnAssign:
        pass


class NoTypesChecker(object):
    """
    A flake8 plugin to ban type hints.
    """

    name = "flake8-no-types"
    version = version("flake8-no-types")

    def __init__(self, tree, *args, **kwargs):
        self.tree = tree

    message_NT001 = "NT001 No type hints."

    def run(self):
        for node in ast.walk(self.tree):
            if (
                isinstance(node, AnnAssign)
                or (isinstance(node, ast.arg) and node.annotation is not None)
                or (isinstance(node, ast.FunctionDef) and node.returns is not None)
            ):
                yield (node.lineno, node.col_offset, self.message_NT001, type(self))
