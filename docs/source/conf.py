# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AttentionMe'
copyright = '2024, Looking-4-Attention'
author = 'Aenoc Woo, Dami Lee, Namhoon Cho, Hyunsoo Kim'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'myst_parser',
]
source_suffix = ['.rst', '.md']
master_doc = 'index'
templates_path = ['_templates']
exclude_patterns = []
language = 'en'
locale_dirs = ['locale']


import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
