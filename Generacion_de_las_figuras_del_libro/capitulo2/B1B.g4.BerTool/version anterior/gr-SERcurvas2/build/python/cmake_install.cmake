# Install script for directory: /home/astrid/gr-SERcurvas2/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/SERcurvas2" TYPE FILE FILES
    "/home/astrid/gr-SERcurvas2/python/__init__.py"
    "/home/astrid/gr-SERcurvas2/python/e_BER_tool.py"
    "/home/astrid/gr-SERcurvas2/python/e_canal_BER.py"
    "/home/astrid/gr-SERcurvas2/python/e_canal_SER.py"
    "/home/astrid/gr-SERcurvas2/python/e_canal_2.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/SERcurvas2" TYPE FILE FILES
    "/home/astrid/gr-SERcurvas2/build/python/__init__.pyc"
    "/home/astrid/gr-SERcurvas2/build/python/e_BER_tool.pyc"
    "/home/astrid/gr-SERcurvas2/build/python/e_canal_BER.pyc"
    "/home/astrid/gr-SERcurvas2/build/python/e_canal_SER.pyc"
    "/home/astrid/gr-SERcurvas2/build/python/e_canal_2.pyc"
    "/home/astrid/gr-SERcurvas2/build/python/__init__.pyo"
    "/home/astrid/gr-SERcurvas2/build/python/e_BER_tool.pyo"
    "/home/astrid/gr-SERcurvas2/build/python/e_canal_BER.pyo"
    "/home/astrid/gr-SERcurvas2/build/python/e_canal_SER.pyo"
    "/home/astrid/gr-SERcurvas2/build/python/e_canal_2.pyo"
    )
endif()

