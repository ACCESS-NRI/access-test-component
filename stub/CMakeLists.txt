cmake_minimum_required(VERSION 3.20)

project(my_project DESCRIPTION "Stub test program"
        LANGUAGES Fortran)

set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -O2 -g")
set(CMAKE_Fortran_FLAGS_DEBUG "")
set(CMAKE_Fortran_FLAGS_RELEASE "")

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE "Release")
endif()

find_package(MPI REQUIRED)

message("---- MPI_Fortran_COMPILER: " ${MPI_Fortran_COMPILER})
set(CMAKE_Fortran_COMPILER ${MPI_Fortran_COMPILER})
message("---- CMAKE_Fortran_COMPILER: " ${CMAKE_Fortran_COMPILER})

# Source code
add_executable(hello_world.exe)
target_sources(hello_world.exe
               src/hello_world.f90
)
target_link_libraries(hello_world.exe)

install(TARGETS hello_world.exe     DESTINATION "bin")
