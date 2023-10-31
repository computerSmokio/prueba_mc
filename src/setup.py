from setuptools import setup
from Cython.Build import cythonize

sources = [
    "src/api/*.py",
    "src/api/resources/*.py",
]

setup(
    ext_modules=cythonize(sources),
    script_args=['build_ext', '-b', 'build'],  # Set the output directory to 'build'
)
