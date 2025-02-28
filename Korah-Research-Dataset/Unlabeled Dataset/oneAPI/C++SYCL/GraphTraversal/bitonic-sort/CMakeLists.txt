# required cmake version
cmake_minimum_required(VERSION 3.5)


if(WIN32)
        set(CMAKE_CXX_COMPILER "icx-cl")
else()
        set(CMAKE_CXX_COMPILER "icpx")
endif()

project (bitonic-sort)

# Set default build type to RelWithDebInfo if not specified
if (NOT CMAKE_BUILD_TYPE)
    message (STATUS "Default CMAKE_BUILD_TYPE not set using Release with Debug Info")
    set (CMAKE_BUILD_TYPE "RelWithDebInfo" CACHE
        STRING "Choose the type of build, options are: None Debug Release RelWithDebInfo MinSizeRel"
        FORCE)
endif()

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -fsycl -std=c++17 -fsycl")

set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -lOpenCL -lsycl")

add_executable (bitonic-sort src/bitonic-sort.cpp)

add_custom_target (run
        COMMAND bitonic-sort 21 47
        WORKING_DIRECTORY ${CMAKE_PROJECT_DIR}
)

