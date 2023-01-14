# Require a modern version of CMake.
CMAKE_MINIMUM_REQUIRED(VERSION 3.0.0 FATAL_ERROR)
PROJECT(mcdft)

# Set default build type.
IF(NOT CMAKE_BUILD_TYPE) 
    SET(CMAKE_BUILD_TYPE Release)
ENDIF()

# Additional flags for special builds.
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall")

# Enable C++11 standard.
IF(NOT CMAKE_VERSION VERSION_LESS "3.1")
    SET(CMAKE_CXX_STANDARD 11)
    SET(CMAKE_CXX_STANDARD_REQUIRED ON)
ELSE()
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
ENDIF()

# Add third-party libraries.
SET(Catch2_INCLUDE_DIRS "src/ext/Catch2" )
INCLUDE_DIRECTORIES(${Catch2_INCLUDE_DIRS})

# SET( EIGEN3_INCLUDE_DIR "src/3rdparty/eigen3/" )
# INCLUDE_DIRECTORIES(${EIGEN3_INCLUDE_DIR})

# Add main sources.
ADD_SUBDIRECTORY(src)
