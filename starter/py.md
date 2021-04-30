
# py

## Virtual Environments

>Using [venv]:

✅<span color="green">**[GOOD]**</span>

|Unix/macOS|Windows|
|-|-|
|python3 -m venv `<DIR>`<br>`source <DIR>`/bin/activate|py -m venv `<DIR>`<br>`<DIR>`\Scripts\activate|

>Using [virtualenv](https://packaging.python.org/key_projects/#virtualenv):

❌<span color="red">**[BAD]**</span>

|Unix/macOS|Windows|
|-|-|
|python3 -m virtualenv `<DIR>`<br>`source <DIR>`/bin/activate|virtualenv `<DIR>`<br>`<DIR>`\Scripts\activate|

To install virtualenv, you can do :
```
pipx install virtualenv
virtualenv --help
```
[Pipx](https://pypi.org/project/pipx/) is provided by a Python 3.5+ interpreter.

For more information, see the [venv] docs or the [virtualenv] docs.

[venv]:https://docs.python.org/3/library/venv.html
[virtualenv]:http://virtualenv.pypa.io/

## commands

### Upgrade pip:
On Windows, as below:
```sh
py -m pip --version
python -m pip install --upgrade pip
```

### Install pipx
On Windows, as below:
```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx completions
```

On macOS, as below:
```sh
brew install pipx
pipx ensurepath
```

### Install virtualenv
On Windows, as below:
```sh
py -m pipx --version
pipx list
pipx install virtualenv
```