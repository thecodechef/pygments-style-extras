README
======

Pygments port of Github Color Scheme.

Install
=======

Using PyPI and pip
------------------

::

    $ (sudo) pip install pygments-style-extras


Manual
------

::

    $ git clone git://github.com/thecodechef/pygments-style-extras.git
    $ cd pygments-style-extras
    $ (sudo) python setup.py install


Usage example
=============

::

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='github').style
    <class 'pygments_style_github.GithubStyle'>


Export the style as CSS
========================

::

    $ pygmentize -S [style] -f html -a .parent > [style].css

Available Styles
----------------
- github
- monokai_light
- railscasts
- ``and Many Nore on the way``

Github Example
----------------

::

    $ pygmentize -S github -f html -a .highlight > github.css


Output:

::

    .highlight .hll { background-color: #ffffcc }
    .highlight  { background: #ffffff; }
    .highlight .c { color: #999988; font-style: italic } /* Comment */
    ...



Extra information
=================

Pygments supported languages
----------------------------

Pygments at the moment supports over 150 different programming languages,
template languages and other markup languages. To see an exhaustive list of the
currently supported languages, use the command::

    $ pygmentize -L lexers

Pygments styles avaible
-----------------------

To get a list of all available stylesheets, execute the following command on the
command line::

    $ pygmentize -L styles

Please read the `official documentation`_ for further information on the usage
of pygment styles.

.. _official documentation: http://pygments.org/docs/
