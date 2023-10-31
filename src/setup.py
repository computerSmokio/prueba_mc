from setuptools import setup 
from shutil import copyfile
from pathlib import Path
from Cython.Build import cythonize

sources = [
    "src/api/*.py",
    "src/api/resources/*.py",
]

setup(
    ext_modules=cythonize(sources),
    script_args=['build_ext', '-b', 'build'],  # Set the output directory to 'build'
)
# copy main.py to build
copyfile('src/main.py', 'build/main.py')
Path('build/static/v1').mkdir(parents=True, exist_ok=False)
copyfile('src/static/v1/swagger.json', 'build/static/v1/swagger.json')