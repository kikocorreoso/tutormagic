"""
==========
tutormagic
==========

Magics to display pythontutor.com in the notebook.

Usage
=====

To enable the magics below, execute ``%load_ext tutormagic``.

``%%tutormagic``

{tutormagic_DOC}

"""

#-----------------------------------------------------------------------------
# Copyright (C) 2015 Kiko Correoso and the pythontutor.com developers
#
# Distributed under the terms of the MIT License. The full license is in
# the file LICENSE, distributed as part of this software.
#
# Contributors:
#   kikocorreoso
#-----------------------------------------------------------------------------

import warnings
warnings.simplefilter("always")
import sys
if sys.version_info.major == 2 and sys.version_info.minor == 7:
    from urllib import quote
elif sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from urllib.parse import quote
else:
    warnings.warn("This extension has not been tested on this Python version", UserWarning)
    
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.testing.skipdoctest import skip_doctest
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)
from IPython.utils.text import dedent
from IPython.display import display, IFrame

@magics_class
class TutorMagics(Magics):
    """
A magic function to show pythontutor.com frame from a code cell.

    """
    def __init__(self, shell):
        super(TutorMagics, self).__init__(shell)

    @skip_doctest
    @magic_arguments()
    @argument(
        '-l', '--lang', action='store', nargs = 1,
        help="Possible languages to be displayed within the iframe. Possible values are: "
             "python2, python3, java, javascript"
        )
    
    #@needs_local_scope
    @argument(
        'code',
        nargs='*',
        )
    @cell_magic
    def tutor(self, line, cell=None, local_ns=None):
        '''
Create an iframe embedding the pythontutor.com page 
with the code included in the code cell::

In [1]: %%tutor -l 'python3'
....: a = 1
....: b = 1
....: a + b

[You will see an iframe with the pythontutor.com page including the code above]
'''
        args = parse_argstring(self.tutor, line)

        if args.lang:
            if args.lang[0] in ['python2', 'python3', 'java', 'javascript']:
                lang = args.lang[0]
            else:
                raise ValueError("{} not supported. Only the following options are allowed: "
                                 "'python2', 'python3', 'java', 'javascript'".format(args.lang[0]))
        else:
            lang = "python3"
        
        url = "http://pythontutor.com/iframe-embed.html#code="
        url += quote(cell)
        url += "&origin=opt-frontend.js&cumulative=false&heapPrimitives=false"
        url += "&textReferences=false&"
        if lang == "python3":
            url += "py=3&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        if lang == "python2":
            url += "py=2&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        if lang == "java":
            url += "py=java&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        if lang == "javascript":
            url += "py=js&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=50%25&codeDivHeight=100%25"
        
        # Display the results in the output area
        display(IFrame(url, height = 350, width = "90%"))
        
__doc__ = __doc__.format(
    tutormagic_DOC = dedent(TutorMagics.tutor.__doc__))

def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(TutorMagics)
