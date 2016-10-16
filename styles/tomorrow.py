# -*- coding: utf-8 -*-
"""
tomorrow
---------------------
Port of the Tomorrow colour scheme
https://github.com/chriskempson/tomorrow-theme
"""

from pygments.style import Style
from pygments.token import Keyword
from pygments.token import Name
from pygments.token import Comment
from pygments.token import String
from pygments.token import Error
from pygments.token import Text
from pygments.token import Number
from pygments.token import Operator
from pygments.token import Generic
from pygments.token import Whitespace
from pygments.token import Punctuation
from pygments.token import Other
from pygments.token import Literal


class TomorrowStyle(Style):

    """
    Port of the Tomorrow colour scheme
    https://github.com/chriskempson/tomorrow-theme
    """

    default_style = ''

    background_color = '#fff'
    highlight_color = '#d6d6d6'

    styles = {
        Text:                      '#4d4d4c',
        Whitespace:                '',
        Error:                     '#c82829',
        Other:                     '',

        Comment:                   '#8e908c',
        Comment.Multiline:         '',
        Comment.Preproc:           '',
        Comment.Single:            '',
        Comment.Special:           '',

        Keyword:                   '#8959a8',
        Keyword.Constant:          '',
        Keyword.Declaration:       '',
        Keyword.Namespace:         '#3e999f',
        Keyword.Pseudo:            '',
        Keyword.Reserved:          '',
        Keyword.Type:              '#eab700',

        Operator:                  '#3e999f',
        Operator.Word:             '',

        Punctuation:               '#4d4d4c',

        Name:                      '#4d4d4c',
        Name.Attribute:            '#4271ae',
        Name.Builtin:              '',
        Name.Builtin.Pseudo:       '',
        Name.Class:                '#eab700',
        Name.Constant:             '#c82829',
        Name.Decorator:            '#3e999f',
        Name.Entity:               '',
        Name.Exception:            '#c82829',
        Name.Function:             '#4271ae',
        Name.Property:             '',
        Name.Label:                '',
        Name.Namespace:            '#eab700',
        Name.Other:                '#4271ae',
        Name.Tag:                  '#3e999f',
        Name.Variable:             '#c82829',
        Name.Variable.Class:       '',
        Name.Variable.Global:      '',
        Name.Variable.Instance:    '',

        Number:                    '#f5871f',
        Number.Float:              '',
        Number.Hex:                '',
        Number.Integer:            '',
        Number.Integer.Long:       '',
        Number.Oct:                '',

        Literal:                   '#f5871f',
        Literal.Date:              '#718c00',

        String:                    '#718c00',
        String.Backtick:           '',
        String.Char:               '#4d4d4c',
        String.Doc:                '#8e908c',
        String.Double:             '',
        String.Escape:             '#f5871f',
        String.Heredoc:            '',
        String.Interpol:           '#f5871f',
        String.Other:              '',
        String.Regex:              '',
        String.Single:             '',
        String.Symbol:             '',

        Generic:                   '',
        Generic.Deleted:           '#c82829',
        Generic.Emph:              'italic',
        Generic.Error:             '',
        Generic.Heading:           'bold #4d4d4c',
        Generic.Inserted:          '#718c00',
        Generic.Output:            '',
        Generic.Prompt:            'bold #8e908c',
        Generic.Strong:            'bold',
        Generic.Subheading:        'bold #3e999f',
        Generic.Traceback:         '',
    }
