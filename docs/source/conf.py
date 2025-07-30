# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../../Codex'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Return of the Bird Tribes'
copyright = '2025, Ethan Womack'
author = 'Ethan Womack'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "myst_parser",
]

# Use read-the-docs theme
html_theme = "sphinx_rtd_theme"

# Recognize Markdown files
source_suffix = {
  '.rst': 'restructuredtext',
  '.md' : 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = []
html_search = False
gettext_compact = False
html_copy_source = False
html_extra_path = []
locale_dirs = []
add_module_names = False
