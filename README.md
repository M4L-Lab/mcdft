# Welcome to mcdft_structure

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Release](https://img.shields.io/pypi/v/mcdftstructure.svg)](https://pypi.org/project/mcdftstructure)
[![Documentation Status](https://readthedocs.org/projects/None/badge/)](https://None.readthedocs.io/)



# Prerequisites

Building mcdft_structure requires the following software installed:

* A C++11-compliant compiler
* CMake `>= 3.9`
* Doxygen (optional, documentation building is skipped if missing)* Python `>= 3.8` for building Python bindings

# Building mcdft_structure

The following sequence of commands builds mcdft_structure.
It assumes that your current working directory is the top-level directory
of the freshly cloned repository:

```
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

The build process can be customized with the following CMake variables,
which can be set by adding `-D<var>={ON, OFF}` to the `cmake` call:

* `BUILD_TESTING`: Enable building of the test suite (default: `ON`)
* `BUILD_DOCS`: Enable building the documentation (default: `ON`)
* `BUILD_PYTHON`: Enable building the Python bindings (default: `ON`)


If you wish to build and install the project as a Python project without
having access to C++ build artifacts like libraries and executables, you
can do so using `pip` from the root directory:

```
python -m pip install .
```

# Testing mcdft_structure

When built according to the above explanation (with `-DBUILD_TESTING=ON`),
the C++ test suite of `mcdft_structure` can be run using
`ctest` from the build directory:

```
cd build
ctest
```

The Python test suite can be run by first `pip`-installing the Python package
and then running `pytest` from the top-level directory:

```
python -m pip install .
pytest
```

# Documentation

mcdft_structure provides a Sphinx-based documentation, that can
be browsed [online at readthedocs.org](https://mcdft-structure.readthedocs.io).
To build it locally, first ensure the requirements are installed by running this command from the top-level source directory:

```
pip install -r doc/requirements.txt
```

Then build the sphinx documentation from the top-level build directory:

```
cmake --build . --target sphinx-doc
```

The web documentation can then be browsed by opening `doc/sphinx/index.html` in your browser.
