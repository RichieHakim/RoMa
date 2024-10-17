from setuptools import setup, find_packages
from pathlib import Path

## Get the parent directory of this file
dir_parent = Path(__file__).parent

with open(str(dir_parent / "roicat" / "__init__.py"), "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().replace("\"", "").replace("\'", "")
            break

setup(
    name="romatch",
    packages=find_packages(include=("romatch*",)),
    version=version,
    author="Johan Edstedt",
    install_requires=open("requirements.txt", "r").read().split("\n"),
)
