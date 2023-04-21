# mcdft_structure - Efficient Monte Carlo Simulation for High Entropy Alloy Systems

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Release](https://img.shields.io/pypi/v/mcdftstructure.svg)](https://pypi.org/project/mcdftstructure)
[![Documentation Status](https://readthedocs.org/projects/None/badge/)](https://None.readthedocs.io/)

## Introduction

Welcome to mcdft_structure! This open-source Python code is designed to provide an efficient solution for Monte Carlo simulation of high entropy alloy systems using a novel and highly efficient machine learning method. Our approach is inspired by the cluster expansion technique while overcoming its limitations by incorporating first-principles Density Functional Theory (DFT) calculations when necessary.

## Features

- Efficient Monte Carlo simulation for high entropy alloy systems.
- Enhanced cluster expansion technique with DFT calculations.
- Seamless integration of DFT calculations into the simulation process.
- Open-source and Python-based for ease of use and customization.

## Prerequisites

Before building mcdft_structure, make sure you have the following software installed:

- A C++11-compliant compiler
- CMake (version >= 3.9)
- Doxygen (optional, for documentation building)
- Python (version >= 3.8) for building Python bindings

## Building mcdft_structure

To build mcdft_structure, follow these steps:

1. Clone the repository.
2. Navigate to the top-level directory of the cloned repository.
3. Run the following commands:

```bash
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```
To install the project as a Python package without C++ build artifacts, use the following command:
```python
python -m pip install .
```

## Testing mcdft_structure
To run the C++ test suite, use ctest from the build directory:

```bash
cd build
ctest
```
To run the Python test suite, first install the Python package using pip, and then run pytest from the top-level directory:

```bash
python -m pip install .
pytest
```

## Documentation
mcdft_structure provides a Sphinx-based documentation, available online at readthedocs.org. To build it locally, follow these steps:

- Ensure the requirements are installed by running this command from the top-level source directory:
```bash
Copy code
pip install -r doc/requirements.txt
```
Build the Sphinx documentation from the top-level build directory:
```bash
Copy code
cmake --build . --target sphinx-doc
```
You can browse the web documentation by opening "doc/sphinx/index.html" in your browser.

Enjoy using mcdft_structure for your Monte Carlo simulations of high entropy alloy systems!
