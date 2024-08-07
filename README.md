# **pyexecute**

## *Description*

`pyexecute` is a python package that facilitates the conversion of python files (`.py`) to executable (`.exe`).

## *Features*

- The package installs the `pyinstaller`
- Delete unnecessary files and folders
- You can overwrite your old executables
- It's only for Windows users

## *Installation*

```bash
pip install git+https://github.com/fernandoluiz2003/pyexecute.git
``` 

## *Usage*

To use the package, you need to have an virtualenv in the directory of your project.

```sh
pyexecute <script_path> [--venv <venv_path>] [--overwrite]
```

- **script_path:** The path to the python file.
- **venv:** ***(optional)*** The venv path is optional.
- **overwrite:** ***(optional)*** A flag to allow overwriting.