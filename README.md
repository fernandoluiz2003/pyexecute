# **pyexecute**

## *Description*

`pyexecute` is a python package that facilitates the conversion of python files (`.py`) to executable (`.exe`).

## *Features*
**1. Virtual Environment Management:**
   - Automatically detects if a script is being run within a virtual environment.
   - Activates a specified virtual environment if not already active.

**2. Script Execution:**
   - Executes a given Python script using `PyInstaller` to create a standalone executable.
   - Ensures the script is executed within the correct environment and with the necessary dependencies.

**3. PyInstaller Integration:**
   - Checks for the presence of `PyInstaller` and installs it if not already available.
   - Uses `PyInstaller` to bundle the specified script into a single executable file.

**4. Command-Line Interface (CLI):**
   - Provides a simple CLI for users to specify the script to be executed and the virtual environment to be used.
   - Supports additional options such as allowing overwrite of existing files.

**5. File Management:**
   - Copies the generated executable to the specified directory.
   - Cleans up build artifacts created during the `PyInstaller` process.

**6. Error Handling:**
   - Provides comprehensive error handling to manage issues such as missing scripts, failed installations, and execution errors.

## *Installation*
It is recommended to install in a global environment to ensure that the `pyexecute` command is available system-wide.

```sh
pip install git+https://github.com/fernandoluiz2003/pyexecute.git
``` 

After the installation, you need to add the `Scripts` directory to the **PATH** to use the commands from any directory.

1. Locate the `Scripts` directory:

```sh
C:\Users\<YourUsername>\AppData\Local\Packages\PythonSoftwareFoundation.Python.<Version>\LocalCache\local-packages\Python<Version>\Scripts
```

2. Add to **PATH**:

- Open the Start Menu, search for ***Environment Variables***, and select "Edit the system environment variables".

- In the System Properties window, click on the ***Environment Variables*** button.
 
- Under ***System variables***, scroll down and find the **Path** variable, then select it and click "Edit."

- Click "New" and paste the path to the Scripts directory.

- Click "OK" to close all windows.

## *Usage*

To use the package, you need to have an virtualenv in the directory of your project.

```sh
pyexecute <script_path> [--venv <venv_path>] [--overwrite]
```

- **script_path:** The path to the python file.
- **venv:** ***(optional)*:** The path to the venv folder. If *default*, it will try to find the virtual environment in the directory.
- **overwrite:** ***(optional)*:** A flag to allow overwriting. If *default:*, overwrite is False.

## *Why did i create this?*

The main reason is to simplify the process of managing virtual environments and running Python scripts, making it a valuable tool for developers who frequently work with different environments and need to generate independent executables.



<div align="center">
   <img src="img/gato_maluco.gif"/>
   <h5> - <b><em>"ngl it's for lazy people like me :)"<h5/>
<div/>
