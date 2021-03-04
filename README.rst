tutormagic extension for the Jupyter notebook
=============================================

Recommendation
==============

Have a look to `nbtutor <https://github.com/lgpage/nbtutor>`_, a more polished and better solution.

-------------------------------------------------------------------------

Jupyter notebook magics to embed http://www.pythontutor.com within an IFrame in
the Jupyter notebook or to open a new tab in the browser using the code from a
notebook code cell (using the IPython kernel).

Install
-------

.. code:: python

    pip install tutormagic
    
or with conda

.. code:: python

    conda install -c kikocorreoso tutormagic

or (for the development version)

.. code:: python

    pip install git+https://github.com/kikocorreoso/tutormagic.git

Tested on Python 2.7.x/3.4.x/3.5.x/3.6.x/3.7.x/3.8.x/3.9.x and Jupyter 3.x/4.x/5.x/6.x.

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

``--lang`` or ``-l``: it allows you to
choose one of the available languages supported by
`pythontutor <http://www.pythontutor.com>`__. If this option is not used then
it will consider the code in the cell as Python3 code.

-  ``%%tutor --lang python3`` or ``%%tutor -l python3`` or ``%%tutor``
   to show a pythontutor IFrame with **python3** code.
-  ``%%tutor --lang python2`` or ``%%tutor -l python2`` to show a
   pythontutor IFrame with **python2** code.
-  ``%%tutor --lang py3anaconda`` or ``%%tutor -l py3anaconda`` to show a
   pythontutor IFrame with **py3anaconda** code. This option allows you to import libs like `numpy`. This is experimental.
-  ``%%tutor --lang java`` or ``%%tutor -l java`` to show a pythontutor
   IFrame with **java** code.
-  ``%%tutor --lang javascript`` or ``%%tutor -l javascript`` to show a
   pythontutor IFrame with **javascript** code.
-  ``%%tutor --lang typescript`` or ``%%tutor -l typescript`` to show a 
   pythontutor IFrame with **typescript** code.
-  ``%%tutor --lang ruby`` or ``%%tutor -l ruby`` to show a 
   pythontutor IFrame with **ruby** code.
-  ``%%tutor --lang c`` or ``%%tutor -l c`` to show a 
   pythontutor IFrame with **c** code.
-  ``%%tutor --lang c++`` or ``%%tutor -l c++`` to show a 
   pythontutor IFrame with **c++** code.
 
 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/normal.png
   :width: 500 px

``--height`` or ``-h``: it changes the height of the output area display in pixels. It is used to define the height of the IFrame used to embed http://pythontutor.com within the notebook. If the `--tab` option is used 
this option will be ignored.

 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/height.png
   :width: 500 px

``--tab`` or ``-t``: it will open http://pythontutor.com in a new tab 
instead of within an IFrame within the notebook.

``--secure`` or ``-s``: it will use HTTPS to open PythonTutor.com. This is useful when being used in a notebook that uses SSL.

``--link`` or ``-k``: it will display a link to PythonTutor, not via an iFrame.

 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/link1.png
   :width: 500 px

``--run`` or ``-r``: Use this option if you also want to run the code in the cell in the notebook.

 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/run1.png
   :width: 500 px

You can customize how PythonTutor is rendered via the options available below in the URL params. The following options are available:

- Use the ``--cumulative`` option to tell PythonTutor to the cumulative to True

 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/cumulative1.png
   :width: 500 px

- Use the ``--heapPrimitives`` option to tell PythonTutor to render objects on the heap
  
 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/test_heap1.png
   :width: 500 px

- Use the ``--textReferences`` option to tell PythonTutor to use text labels for references
- Use the ``--curInstr`` followed by a number to start the visualisation at the defined step
  
 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/current1.png
   :width: 500 px

- Use the ``--verticalStack`` to set visualization to stack atop one another.
  
 .. image:: https://raw.githubusercontent.com/kikocorreoso/tutormagic/master/imgs/vertical1.png
   :width: 500 px

Examples
--------

`Example notebook included in the repository <http://nbviewer.jupyter.org/github/kikocorreoso/tutormagic/blob/master/examples/Examples.ipynb>`__.

`Example (in spanish)
notebook <http://nbviewer.ipython.org/github/Pybonacci/notebooks/blob/master/tutormagic.ipynb>`__.

Name of the extension
---------------------

The name of the extension was suggested by Doug S. Blank 
(`@dsblank <https://github.com/dsblank>`__).

Changelog
---------

Version 0.3.1
-------------

- Added option `--lang py3anaconda` (thanks to `@naereen <https://github.com/naereen>`__).

Version 0.3.0
~~~~~~~~~~~~~

- Added options ``--secure``, ``--link``, ``--cumulative``, ``--heapPrimitives`` and ``--textReferences`` (thanks to James Quacinella (`@jquacinella <https://github.com/jquacinella>`__)).
- Added options ``--run``, ``--curInstr`` and ``--verticalStack``.

Version 0.2.0
~~~~~~~~~~~~~

-  Added new ``--tab`` option (thanks to Holger Karl (`@hkarl <https://github.com/hkarl>`__)).
-  Added new ``--height`` option (thanks to Tom Simonart(`@tomsimonart <https://github.com/tomsimonart>`__)).
-  Added new languages available on http://pythontutor.com (Typescript, Ruby, C and C++).

Version 0.1.0
~~~~~~~~~~~~~

-  Initial version
