tutormagic extension for the IPython notebook
==========================================

IPython magics to embed http://www.pythontutor.com within an IFrame in
the IPython notebook using the code from an IPython code cell.

Install
-------

.. code:: python

    pip install tutormagic

or

.. code:: python

    pip install git+https://github.com/kikocorreoso/tutormagic.git

Tested on Python 2.7 and Python 3.4 and IPython 3.0.0.

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

Options
-------

The only available option is the ``--lang`` or ``-l`` that allows you to
choose one othe the available languages supported by
`pythontutor <http://www.pythontutor.com>`__

-  ``%%tutor --lang python3`` or ``%%tutor -l python3`` or
   ``%%tutor`` to show a pythontutor IFrame with python3 code.
-  ``%%jupytor --lang python2`` or ``%%tutor -l python2`` to show a
   pythontutor IFrame with python2 code.
-  ``%%tutor --lang java`` or ``%%tutor -l java`` to show a
   pythontutor IFrame with java code.
-  ``%%tutor --lang javascript`` or ``%%tutor -l javascript`` to
   show a pythontutor IFrame with javascript code.
