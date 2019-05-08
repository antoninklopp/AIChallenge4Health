#Minimum version of CMake
cmake_minimum_required(VERSION 3.9) 

include_directories(library)
# add_library(rescaling SHARED rescaling.cpp)

add_executable(rescaling rescaling.cpp)

target_link_libraries(rescaling ${OpenCV_LIBS})