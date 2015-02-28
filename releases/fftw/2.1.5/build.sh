#!/bin/bash
./configure --prefix=$PREFIX --infodir=$PREFIX/infodocs
make -j$(getconf _NPROCESSORS_ONLN)
make install
