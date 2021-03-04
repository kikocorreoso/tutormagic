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

__version__="0.3.1"

#-----------------------------------------------------------------------------
# Copyright (C) 2015-2017 Kiko Correoso and the pythontutor.com developers
#
# Distributed under the terms of the MIT License. The full license is in
# the file LICENSE, distributed as part of this software.
#
# Contributors:
#   kikocorreoso, jquacinella, hkarl, naereen, tomsimonart
#-----------------------------------------------------------------------------

import webbrowser
import warnings
warnings.simplefilter("always")
import sys
if sys.version_info.major == 2 and sys.version_info.minor == 7:
    from urllib import quote
elif sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from urllib.parse import quote
else:
    warnings.warn("This extension has not been tested on this Python version", 
                  UserWarning)

from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.testing.skipdoctest import skip_doctest
from IPython.core.magic_arguments import (argument, magic_arguments,
                                          parse_argstring)
from IPython.utils.text import dedent
from IPython.display import display, IFrame, HTML

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
        help="Languages to be displayed within the iframe or in a new tab. "
             "Possible values are: "
             "python2, python3, py3anaconda, java, javascript, typescript, ruby, c, c++"
        )

    @argument(
        '-h', '--height', action='store', nargs=1,
        help="Change the height of the output area display in pixels"
        )

    @argument(
        '-t', '--tab', action='store_true',
        help="Open pythontutor in a new tab",
        )

    @argument(
        '-s', '--secure', action='store_true',
        help="Open pythontutor using https in a new tab",
        )

    @argument(
        '-k', '--link', action='store_true',
        help="Just display a link to pythontutor",
        )
        
    @argument(
        '-r', '--run', action='store_true',
        help="Run the cell code also in the notebook",
        )

    @argument(
        '--cumulative', action='store_true', default=False,
        help="PythonTutor config: Set the cumulative option to True", 
        )
    
    @argument(
        '--heapPrimitives', action='store_true', default=False,
        help="PythonTutor config: Render objects on the heap", 
        )
    
    @argument(
        '--textReferences', action='store_true', default=False,
        help="PythonTutor config: Use text labels for references", 
        )

    @argument(
        '--curInstr', action='store', default=0,
        help="PythonTutor config: Start at the defined step", 
        )
        
    @argument(
        '--verticalStack', action='store_true', default=False,
        help="Set visualization to stack atop one another", 
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

        [You will see an iframe with the pythontutor.com page including the 
        code above]
        '''
        args = parse_argstring(self.tutor, line)

        if args.lang:
            if args.lang[0].lower() in ['python2', 
                                        'python3',
					'py3anaconda',
                                        'java', 
                                        'javascript',
                                        'typescript',
                                        'ruby',
                                        'c',
                                        'c++']:
                lang = args.lang[0].lower()
            else:
                raise ValueError(
                    "{} not supported. Only the following options are allowed: "
                    "'python2', 'python3', 'py3anaconda', 'java', 'javascript', "
                    "'typescript', 'ruby', 'c', 'c++'".format(args.lang[0]))
        else:
            lang = "python3"

        # Sometimes user will want SSL pythontutor site if 
        # jupyter/hub is using SSL as well
        protocol = 'http://'
        if args.secure:
            protocol = 'https://'

        url = protocol + "pythontutor.com/iframe-embed.html#code="
        url += quote(cell)
        url += "&origin=opt-frontend.js"

        # Add custom pythontutor options, defaults to all false
        url += "&cumulative={}".format(str(args.cumulative).lower())
        url += "&heapPrimitives={}".format(str(args.heapPrimitives).lower())
        url += "&textReferences={}".format(str(args.textReferences).lower())
        url += "&curInstr={}&".format(str(args.curInstr).lower())
        url += "&verticalStack={}&".format(str(args.verticalStack).lower())

        # Setup the language URL param
        if lang == "python3":
            url += "py=3"
        elif lang == "python2":
            url += "py=2"
        elif lang == "py3anaconda":
            url += "py=py3anaconda"
        elif lang == "java":
            url += "py=java"
        elif lang == "javascript":
            url += "py=js"
        elif lang == "typescript":
            url += "py=ts"
        elif lang == "ruby":
            url += "py=ruby"
        elif lang == "c":
            url += "py=c"
        elif lang == "c++":
            url += "py=cpp"
        
        # Add the rest of the misc options to pythontutor
        url += "&rawInputLstJSON=%5B%5D&codeDivWidth=50%25&codeDivHeight=100%25"       

        # Display in new tab, or in iframe, or link to it via anchor link?
        if args.link:
            # Create html link to pythontutor
            css = ("box-sizing: border-box; "
                   "padding: 0 5px; border: "
                   "1px solid #CFCFCF;")
            display(
                HTML(
                    data=(
                        '<div class="text-center"><strong>'
                        '<a style="{0}" target="_" href={1}>Python Tutor</a>'
                        '</strong></div>'.format(css, url)
                    )
                )
            )
        elif args.tab:
            # Open up a new tab in the browser to pythontutor URL
            webbrowser.open_new_tab(url)
        else:
            # Display the results in the output area
            if args.height:
                display(IFrame(
                    url, height = int(args.height[0]), width = "100%"
                ))
            else:
                display(IFrame(url, height = 350, width = "100%"))
        if args.run:
			# Run cell like normal
            self.shell.run_cell(cell)

__doc__ = __doc__.format(
    tutormagic_DOC = dedent(TutorMagics.tutor.__doc__))

def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(TutorMagics)
