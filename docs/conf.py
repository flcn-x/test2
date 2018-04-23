# -*- coding: utf-8 -*-
#
# -- Path setup --------------------------------------------------------------
import sys
import os
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('../'))
# -- Project information -----------------------------------------------------
project = u'test Project'
copyright = u'falcon'
author = 'falcon'
# -- General configuration ---------------------------------------------------
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# -- Options for HTMLHelp output ---------------------------------------------
autoclass_content = "both"
autodoc_member_order = "bysource"
