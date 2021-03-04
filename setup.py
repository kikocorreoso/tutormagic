try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import io
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'jupyter>=1.0',
]

setup(
    name='tutormagic',
    version='0.3.1',
    description='Magic to display pythontutor.com from a code cell in the IPython notebook.',
    long_description=long_description,
    url='https://github.com/kikocorreoso/tutormagic',

    # Author details
    author='Kikocorreoso',
    author_email='',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    # What does your project relate to?
    keywords='ipython jupyter notebook pythontutor.com teaching',

    py_modules=['tutormagic'],
    install_requires=install_requires,
)
