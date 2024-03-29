# CHANGELOGS

## Table of Contents
- [2023-12-24](#2023-12-24)
    + 1019H : v0.1.0
- [2024-01-31](#2024-01-31)
- [2024-02-02](#2024-02-02)
    + 0003H : v0.2.0
    + 0021H : v0.2.1
    + 0030H : v0.2.2

## Logs
### 2023-12-24
#### 0945H
- New
    - Created directory 'package' for holding the AndroidProjectGenerator framework/library classes, functions and attributes
        - Added source file 'apg.py' as the main library
        - Added source file 'apg_latest.py' as a latest development branch
        - Added source file 'apg_stable.py' as a stable branch
- Updates
    - Modified source file 'generator.py'
        - Migrated class AndroidProjectGenerator and related contents into source library 'package/apg.py'
        - Implemented CLI argument parsing
        - Added Platform recognition that determines if system is Windows or Linux before initializing the APG system classes based on the operating system
        - Updated documentationa and usage
- TODO
    - Clean-up and convert 'apg_latest.py' to 'apg.py'

#### 1019H
- Updates
    - Replaced 'apg_stable.py' with the latest release of 'apg.py'

### 2024-01-31
#### 1316H
- Added new features
    - Packaging and Deployment:
        - Able to install android-project-generator from python 
            - using pip
                - Directly from github
                    ```console
                    pip install git+https://github.com/Thanatisia/android-project-generator/tree/development/app/languages/python
                    ```
                - Locally in development mode
                    - Clone repository
                        ```console
                        git lcone https://github.com/Thanatisia/android-project-generator
                        ```
                    - Change directory into python directory
                        ```console
                        cd app/languages/python
                        ```
                    - Install locally in development/editable mode
                        ```console
                        pip install .
                        ```

- New
    - Added new document '.gitignore' for the repository
    - Added new script 'setup.py' in 'app/languages/python'
        + This is the setup script for python packaging and deployment using setuptools
    - Added new script 'apg-shell.bat' in 'src/'
        + This is a environment variable shell script to setup the variables required to generate a proper Android project filesystem structure in Windows
    - Added new script 'apg-shell.sh' in 'src/'
        + This is a environment variable shell script to setup the variables required to generate a proper Android project filesystem structure in *NIX environment

- Updates
    - Deleted '__pycache__' directories

#### 1827H
- New
    - Added new document 'BUILD.md' for holding information to build project from source
    - Added new document 'CONTRIBUTING.md' for holding rules and information if someone wants to contribute

### 2024-02-02
#### 0003H
+ v0.2.0
- New
    - Added '__init__.py' to the package directories (src/package-name, src/package-name/package)
- Updates
    - Migrated the previous layout 'src' => into the 'src/[package-name]' best practice project structure layout
        - Renamed generator.py => '__main__'.py : The main entry point runner/launcher file that will be referenced on startup after installation
            - Removed 'if __name__ == "__main__":' from __main__.py because this is an executable application and not a framework/package/library to be imported
                - However, you can still import and use the libraries directly
                    ```python
                    from android_project_generator.package.apg import classes
                    ```

#### 0022H
+ v0.2.1
- Updates
    - Updated README.md with 
        + updated packaging naming convention instead of manual execution
        + Usage example snippets on using package as a dependency

#### 0030H
+ v0.2.2

- Updates
    - Updated '__main__.py' entry point
        + Repositioned dictionary 'application_Info' down
        + Obtained application's executable name only from the executable path
        + Updated the help message display function
        + Cleaned up and removed some print messages

