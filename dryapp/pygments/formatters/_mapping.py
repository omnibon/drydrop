# -*- coding: utf-8 -*-
"""
    pygments.formatters._mapping
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Formatter mapping defintions. This file is generated by itself. Everytime
    you change something on a builtin formatter defintion, run this script from
    the formatters folder to update it.

    Do not alter the FORMATTERS dictionary by hand.

    :copyright: 2006-2007 by Armin Ronacher, Georg Brandl.
    :license: BSD, see LICENSE for more details.
"""

from pygments.util import docstring_headline

# start
from pygments.formatters.html import HtmlFormatter

FORMATTERS = {
    HtmlFormatter: ('HTML', ('html',), ('*.html', '*.htm'), "Format tokens as HTML 4 ``<span>`` tags within a ``<pre>`` tag, wrapped in a ``<div>`` tag. The ``<div>``'s CSS class can be set by the `cssclass` option."),
}

if __name__ == '__main__':
    import sys
    import os

    # lookup formatters
    found_formatters = []
    imports = []
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    for filename in os.listdir('.'):
        if filename.endswith('.py') and not filename.startswith('_'):
            module_name = 'pygments.formatters.%s' % filename[:-3]
            print module_name
            module = __import__(module_name, None, None, [''])
            for formatter_name in module.__all__:
                imports.append((module_name, formatter_name))
                formatter = getattr(module, formatter_name)
                found_formatters.append(
                    '%s: %r' % (formatter_name,
                                (formatter.name,
                                 tuple(formatter.aliases),
                                 tuple(formatter.filenames),
                                 docstring_headline(formatter))))
    # sort them, that should make the diff files for svn smaller
    found_formatters.sort()
    imports.sort()

    # extract useful sourcecode from this file
    f = open(__file__)
    try:
        content = f.read()
    finally:
        f.close()
    header = content[:content.find('# start')]
    footer = content[content.find("if __name__ == '__main__':"):]

    # write new file
    f = open(__file__, 'w')
    f.write(header)
    f.write('# start\n')
    f.write('\n'.join(['from %s import %s' % imp for imp in imports]))
    f.write('\n\n')
    f.write('FORMATTERS = {\n    %s\n}\n\n' % ',\n    '.join(found_formatters))
    f.write(footer)
    f.close()
