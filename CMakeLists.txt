cmake_minimum_required(VERSION 3.10)
project(detectSerial)

set(CMAKE_CXX_STANDARD 14)

find_package(PythonLibs REQUIRED)

include_directories(${PYTHON_INCLUDE_DIRS})

add_executable(detectSerial srcs/EndEffectorSerialMonitor.cpp)
target_link_libraries(detectSerial ${PYTHON_LIBRARIES})