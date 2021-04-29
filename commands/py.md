# py commands

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