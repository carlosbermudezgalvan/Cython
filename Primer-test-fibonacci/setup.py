from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("fib_cy.pyx"))
setup(ext_modules = exts)
