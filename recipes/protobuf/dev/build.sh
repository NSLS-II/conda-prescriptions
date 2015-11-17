#!/bin/bash

./autogen.sh
./configure --prefix=$PREFIX
make -j 8
make check -j 8
make install -j 8

export PKG_CONFIG_PATH=$PREFIX/lib/pkgconfig

cd python
python setup.py -q build_py
python setup.py -q build
python setup.py -q test -q

python setup.py install
