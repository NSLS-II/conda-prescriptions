#!/bin/bash
export PYEPICS_LIBCA=$PREFIX/lib/libca.so.3.15.1
echo $PYEPICS_LIBCA
${PYTHON} setup.py build
${PYTHON} setup.py install
