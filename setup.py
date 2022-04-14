from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="PyPackageTemplate",
    version="0.0.1",
    description="A sample Python project",
    author="Fergus Horrobin",
    author_email="horrobin@astro.utoronto.ca",
    packages=find_packages(),
)