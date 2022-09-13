#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "mcdft-structure/mcdft-structure.hpp"

namespace py = pybind11;

namespace mcdftstructure {

PYBIND11_MODULE(_mcdftstructure, m)
{
  m.doc() = "Python Bindings for mcdft_structure";
  m.def("add_one", &add_one, "Increments an integer value");
}

} // namespace mcdftstructure
