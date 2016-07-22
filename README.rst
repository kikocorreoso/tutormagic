tutormagic extension for the Jupyter notebook
=============================================

IPython magics to embed http://www.pythontutor.com within an IFrame in
the Jupyter notebook or to open a new tab in the browser using the code from an 
IPython code cell (IPython kernel).

Install
-------

.. code:: python

    pip install tutormagic

or

.. code:: python

    pip install git+https://github.com/kikocorreoso/tutormagic.git

Tested on Python 2.7.x, 3.4.x and 3.5.x and IPython/Jupyter 3.x/4.x.

Usage
-----

First, load the extension:

.. code:: python

    %load_ext tutormagic

Once loaded, in a code cell in the notebook type the following:

.. code:: python

    %%tutor --lang python3
    # some python code
    # ...

to create an IFrame within the notebook with the http://www.pythontutor.com page
with the code included in the Jupyter code cell or:

.. code:: python

    %%tutor --lang python3 --tab
    # some python code
    # ...

to open http://www.pythontutor.com page in a new browser tab with the code 
included in the Jupyter code cell.

Options
-------

The available options are ``--lang`` (or ``-l``), ``--height`` (or ``-h``) and 
``--tab`` (or ``-t``):

The ``--lang`` or ``-l`` option allows you to
choose one of the available languages supported by
`pythontutor <http://www.pythontutor.com>`__. It this option is set then
it will consider the code in the cell as Python3 code.

-  ``%%tutor --lang python3`` or ``%%tutor -l python3`` or ``%%tutor``
   to show a pythontutor IFrame with ***python3*** code.
-  ``%%tutor --lang python2`` or ``%%tutor -l python2`` to show a
   pythontutor IFrame with ***python2*** code.
-  ``%%tutor --lang java`` or ``%%tutor -l java`` to show a pythontutor
   IFrame with ***java*** code.
-  ``%%tutor --lang javascript`` or ``%%tutor -l javascript`` to show a
   pythontutor IFrame with ***javascript*** code.
-  ``%%tutor --lang typescript`` or ``%%tutor -l typescript`` to show a 
   pythontutor IFrame with ***typescript*** code.
-  ``%%tutor --lang ruby`` or ``%%tutor -l ruby`` to show a 
   pythontutor IFrame with ***ruby*** code.
-  ``%%tutor --lang c`` or ``%%tutor -l c`` to show a 
   pythontutor IFrame with ***c*** code.
-  ``%%tutor --lang c++`` or ``%%tutor -l c++`` to show a 
   pythontutor IFrame with ***c++*** code.

The ``--height`` or ``-h`` is used to define the height of the IFrame used to 
embed http://pythontutor.com within the notebook. If the `--tab` option is used 
this option will be ignored.

The ``--tab`` or ``-t`` option will open http://pythontutor.com in a new tab 
instead of within an IFrame within the notebook.

Example (in spanish)
--------------------

`Example
notebook <http://nbviewer.ipython.org/github/Pybonacci/notebooks/blob/master/tutormagic.ipynb>`__.

Name of the extension
---------------------

The name of the extension was suggested by Doug S. Blank 
(`@dsblank <https://github.com/dsblank>`__).

Changelog
---------
Version 0.2.0
~~~~~~~~~~~~~

-  Added new ``--tab`` option (thanks to Holger Karl 
(`@hkarl <https://github.com/hkarl>`__)).
-  Added new ``--height`` option (thanks to Tom Simonart(`@tomsimonart <https://github.com/tomsimonart>`__)).
-  Added new languages available on http://pythontutor.com (Typescript, Ruby, C and C++).

Version 0.1.0
~~~~~~~~~~~~~

-  Initial version
