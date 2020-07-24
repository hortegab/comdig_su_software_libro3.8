#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/astrid/gr-SERcurvas2/python
export PATH=/home/astrid/gr-SERcurvas2/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/astrid/gr-SERcurvas2/build/swig:$PYTHONPATH
/usr/bin/python2 /home/astrid/gr-SERcurvas2/python/qa_e_canal_2.py 
