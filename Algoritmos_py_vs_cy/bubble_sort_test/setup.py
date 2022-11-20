from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("bubble_sort_cy.pyx"))
setup(ext_modules = exts)
