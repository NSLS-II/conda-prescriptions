#!/bin/bash

set -e

./configure --prefix=$PREFIX --with-curses
make -j$(getconf _NPROCESSORS_ONLN) SHLIB_LIBS="-lncurses -L$PREFIX/lib"
make install

