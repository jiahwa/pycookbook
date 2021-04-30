
<b>Environment (please complete the following information):</b>
- pip command
- OS and Python version: Windows, python 3.6.0

<b>Describe the bug</b>
```log
PS E:\workspace\yujahuaGitHub\pycookbook> pip
Traceback (most recent call last):
  File "c:\users\zz\appdata\local\programs\python\python36\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\users\zz\appdata\local\programs\python\python36\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "C:\Users\Zz\AppData\Local\Programs\Python\Python36\Scripts\pip.exe\__main__.py", line 5, in <module>
  File "c:\users\zz\appdata\local\programs\python\python36\lib\site-packages\pip\_internal\cli\main.py", line 9, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "c:\users\zz\appdata\local\programs\python\python36\lib\site-packages\pip\_internal\cli\autocompletion.py", line 10, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "c:\users\zz\appdata\local\programs\python\python36\lib\site-packages\pip\_internal\cli\main_parser.py", line 8, in <module>
    from pip._internal.cli import cmdoptions
  File "c:\users\zz\appdata\local\programs\python\python36\lib\site-packages\pip\_internal\cli\cmdoptions.py", line 30, in <module>
    from pip._internal.utils.hashes import STRONG_HASHES
  File "c:\users\zz\appdata\local\programs\python\python36\lib\site-packages\pip\_internal\utils\hashes.py", line 2, in <module>
    from typing import TYPE_CHECKING, BinaryIO, Dict, Iterator, List, NoReturn
ImportError: cannot import name 'NoReturn'
PS E:\workspace\yujahuaGitHub\pycookbook>
```

ImportError: cannot import name 'NoReturn', 
[beets #1666](https://github.com/psf/black/issues/1666)

ImportError: cannot import name 'NoReturn',
[black #3143](https://github.com/beetbox/beets/issues/3143)