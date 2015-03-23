jupytor extension for the IPython notebook
==========================================

IPython magics to embed http://www.pythontutor.com within an IFrame in the IPython notebook using the 
code from an IPython code cell.

## Install

```python
pip install jupytor
```

or 

```python
pip install git+https://github.com/kikocorreoso/jupytor.git
```

## Usage

In a code cell in the notebook type the following:

```python
%%jupytor --lang python3
# some python code
# ...
```

## Options

The only available option is the `--lang` or `-l` that allows you to choose one othe the available languages supported by 
[pythontutor](http://www.pythontutor.com)

* `%%jupytor --lang python3` or `%%jupytor -l python3` or `%%jupytor` to show a pythontutor IFrame with python3 code.
* `%%jupytor --lang python2` or `%%jupytor -l python2` to show a pythontutor IFrame with python2 code.
* `%%jupytor --lang java` or `%%jupytor -l java` to show a pythontutor IFrame with java code.
* `%%jupytor --lang javascript` or `%%jupytor -l javascript` to show a pythontutor IFrame with javascript code.
