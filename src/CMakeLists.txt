add_library(mcdft-structure mcdft-structure.cpp)
target_include_directories(
  mcdft-structure PUBLIC $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include/>
                         $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)
