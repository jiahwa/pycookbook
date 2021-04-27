# pycookbook
cook book for python, make things better to do

## Start with `venv`
Since available by default in Python 3.3+, "Virtual Environments" is a better experience rather than being installed globally.

Basic usage is like so:

>Useing [venv]:

|Unix/macOS|Windows|
|-|-|
|python3 -m venv `<DIR>`<br>`source <DIR>`/bin/activate|py -m venv `<DIR>`<br>`<DIR>`\Scripts\activate|

>Useing [virtualenv](https://packaging.python.org/key_projects/#virtualenv):

|Unix/macOS|Windows|
|-|-|
|python3 -m virtualenv `<DIR>`<br>`source <DIR>`/bin/activate|virtualenv `<DIR>`<br>`<DIR>`\Scripts\activate|

To install virtualenv, you can do :
```
pipx install virtualenv
virtualenv --help
```
Pipx is provided by a Python 3.5+ interpreter

For more information, see the [venv] docs or the [virtualenv] docs.

[venv]:https://docs.python.org/3/library/venv.html
[virtualenv]:http://virtualenv.pypa.io/

## TODO:Get color from an image
- [Pillow](https://pypi.org/project/Pillow/)

## Coding Rules

- [learn rules for python](https://www.python.org/dev/peps/pep-0008/)

## LICENSE
MIT