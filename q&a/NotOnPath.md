<b>Environment (please complete the following information):</b>
- -- user pipx command
- OS and Python version: Windows, python 3.6.0 and 3.9.4

<b>Describe the bug [**warning**]</b>
```log
Installing collected packages: colorama, argcomplete, pyparsing, packaging, click, userpath, pipx
  WARNING: The script userpath.exe is installed in 'C:\Users\Zz\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pipx.exe is installed in 'C:\Users\Zz\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed argcomplete-1.12.3 click-7.1.2 colorama-0.4.4 packaging-20.9 pipx-0.16.2.1 pyparsing-2.4.7 userpath-1.4.2
WARNING: You are using pip version 20.2.3; however, version 21.1.1 is available.
You should consider upgrading via the 'C:\Users\Zz\AppData\Local\Programs\Python\Python39\python.exe -m pip install --upgrade pip' command.
```

<b>Answers</b>

[The script is installed in directory, which is not PATH](https://superuser.com/questions/1372793/the-script-is-installed-in-directory-which-is-not-path)

[Permanently add a directory to PYTHONPATH?](https://stackoverflow.com/questions/3402168/permanently-add-a-directory-to-pythonpath)