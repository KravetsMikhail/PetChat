# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
def setup(app):
    app.add_css_file('css/custom.css')

project = 'Описание архитектуры мессенджера'
project_copyright = 'PetChat'
copyright = '2024 г'
author = 'Кравец М.А.'
version = '0.1.0'
release = '0.1.0'
plantuml = 'java -Djava.awt.headless=true -jar ../../../plantuml-mit-1.2024.5.jar'
# plantuml = 'java -Djava.awt.headless=true -jar /home/docs/checkouts/readthedocs.org/user_builds/petchat/envs/latest/bin/plantuml.jar'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_dark_mode",
    "sphinx_copybutton",
    "sphinxcontrib.httpdomain",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.plantuml",
    "sphinx.ext.graphviz",
    "sphinxcontrib.openapi",
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'groundwork'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "body_max_width": "1200px",
}
html_static_path = ['_static']
html_css_files = [
    "css/custom.css"
]
html_output_encoding = 'utf-8'

graphviz_output_format = 'svg'
html_show_sourcelink = False

