# Build from Source

## Table of Contents
+ [Setup](#setup)
+ [Distribution and Packaging](#distribution-and-packaging)

## Setup
### Pre-Requisites
- Clone repository
    ```console
    git clone https://github.com/Thanatisia/android-project-generator
    ```

- Change directory into repository
    ```console
    cd android-project-generator
    ```

- (Optional) Create Virtual Environments for isolation testing/usage
    - Create the Virtual Environment container
        ```console
        python -m venv env
        ```
    - Chroot and enter Virtual Environment
        - Linux
            ```console
            . env/bin/activate
            ```
        - Windows
            ```console
            .\env\Scripts\activate
            ```

- Change directory into project root directory
    ```console
    cd [project-root-directory]
    ```

## Distribution and Packaging
### Development and Testing
- Install framework using pip
    - Locally as development mode
        ```console
        pip install .
        ```

### Build
#### Using setuptools
- Build/Compile static files
    - Explanation
        + This will compile/"package" the source files into an 'egg', .tar and wheel static files for sharing and installation
    ```console
    python setup.py build
    ```

### Installation
- Local installation
    - Install built static files using setup.py with setuptools
        - Explanation
            + This will install all dependencies, pre-requisites using setup.py and install the framework/package defined in setup.py
        - Install in default location
            - Note
                + This will create the 'dist' directory and install the static distribution files to the 'dist' directory
            ```console
            python setup.py install
            ```
        - Install in custom site-package prefix (location)
            - Note
                - This will create the specified prefix directory and install the static distribution files to that directory location
                    - Directory example
                        + ~/.local : This will install the files in '~/.local/lib/site-packages/[egg-file]'
            ```console
            python setup.py install --prefix [directory]
            ```
    - Install built static distribution files
        - tarball
            ```console
            pip install dist/[package-name]-[version-number].tar.gz
            ```
        - wheel
            ```console
            pip install dist/[package-name]-[version-number]-[python-version].whl
            ```
        - egg file
            ```console
            pip install dist/[package-name]-[version-number]-[python-version].egg
            ```

- Remote installation
    - Install from PyPI (WIP)
        ```console
        pip install android-project-generator
        ```
    - Install from GitHub
        ```console
        pip install git+https://github.com/Thanatisia/android-project-generator{@[branch-tag]}#subdirectory=app/languages/python
        ```

### Confirmation
- Validate package is installed
    ```console
    pip freeze list
    ```

### Post-Installation
- Uninstall package
    ```console
    pip uninstall [package-name]
    ```

## Resources

## References

## Remarks

