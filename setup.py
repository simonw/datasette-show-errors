from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-show-errors",
    description="Datasette plugin for displaying error tracebacks",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-show-errors",
    license="Apache License, Version 2.0",
    version=VERSION,
    entry_points={"datasette": ["show_errors = datasette_show_errors"]},
    py_modules=["datasette_show_errors"],
    install_requires=["starlette", "datasette"],
    extras_require={
        "test": ["pytest"]
    },
)
