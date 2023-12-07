# Python Library for Calculator

This is a simple Python library that provides functionality for addition and subtraction.

## Installation

You can install the library using the following pip command:

```bash
pip install git+https://github.com/rahulmydur29/python_library.git

# Importing the library
from calculator.add.addition import Addition
from calculator.sub.subtraction import Subtraction


You need to follow the below structure, while importing the libraries from github.
'calculator' is the main folder where python files are stored.
'add' and 'sub' is the Sub-Folder of that python files.
'addition' and 'substraction' is the python file name.
'Addition'and 'Subtraction' is the Class name created in the perticular python files


'__int__.py' file has to be is the important file should be there in the every Sub-Folder while creating the Library.

About __init__ :
1. Marks a Directory as a Package: It tells Python that the directory is a package containing Python modules.

2. Enables Initialization: It allows you to execute code when the package is imported, enabling setup tasks and defining package-level elements.

3. Controls the Package's Namespace: It determines what gets imported when the package is used

4. The __init__.py file serves as the entry point for package initialization, managing the package's namespace, enabling package discovery, facilitating versioning, and providing a flexible mechanism for customizing package behavior.

5. Subpackage Setup: Initialize subpackages or submodules within the package for use on import.

6. Metadata & Versioning: Include version information or metadata within the file for easy access.

7. Conditional Logic: Perform conditional imports or checks for compatibility and error handling specific to the package.
