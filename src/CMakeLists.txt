# Require a modern version of CMake.
CMAKE_MINIMUM_REQUIRED(VERSION 3.0.0 FATAL_ERROR)
PROJECT(mcdft)
SET(CMAKE_BUILD_TYPE Release)

# This library depends on the pybind11 framework.
ADD_SUBDIRECTORY("ext/pybind11" pybind11)

# List of source files that need to be compiled:
SET(SourceFiles
  mcdft-structure.cpp
  _mcdft-structure.cpp
)

PYBIND11_ADD_MODULE(_mcdft ${SourceFiles})
SET_TARGET_PROPERTIES(_mcdft PROPERTIES OUTPUT_NAME "_mcdft")


