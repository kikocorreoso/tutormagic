tutormagic extension for the IPython notebook
=============================================

IPython magics to embed http://www.pythontutor.com within an IFrame in the IPython notebook using the 
code from an IPython code cell.

## Install

```python
pip install tutormagic
```

or 

```python
pip install git+https://github.com/kikocorreoso/tutormagic.git
```

Tested on Python 2.7 and Python 3.4 and IPython 3.0.0.

## Usage

First, load the extension:

```python
%load_ext tutormagic
```

Once loaded, in a code cell in the notebook type the following:

```python
%%tutor --lang python3
# some python code
# ...
```

## Options

The only available option is the `--lang` or `-l` that allows you to choose one of the available languages supported by 
[pythontutor](http://www.pythontutor.com)

* `%%tutor --lang python3` or `%%tutor -l python3` or `%%tutor` to show a pythontutor IFrame with python3 code.
* `%%tutor --lang python2` or `%%tutor -l python2` to show a pythontutor IFrame with python2 code.
* `%%tutor --lang java` or `%%tutor -l java` to show a pythontutor IFrame with java code.
* `%%tutor --lang javascript` or `%%tutor -l javascript` to show a pythontutor IFrame with javascript code.

## Example (in spanish)

[Example notebook](http://nbviewer.ipython.org/github/Pybonacci/notebooks/blob/master/tutormagic.ipynb).

## Name of the extension

The name of the extension was suggested by [@dsblank](https://github.com/dsblank).
